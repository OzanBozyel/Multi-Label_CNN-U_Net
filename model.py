"""
@author: Ozan
"""
from keras.models import Model
from keras.layers import Input, Conv2D, MaxPooling2D
from keras.layers import concatenate, Conv2DTranspose,Flatten
from keras.optimizers import Adam
from keras import backend as K
import settings
from tensorflow import keras as K

class MODEL:
    def __init__(self,
                 features_map = settings.FEATURES_MAP,
                 dropout = settings.USE_DROPOUT,
                 dropout_rate = settings.DROPOUT_RATE,
                 smooth = settings.DICE_SMOOTH,
                 learning_rate = settings.LEARNING_RATE,
                 model_print = settings.PRINT,
                 use_dropout = settings.USE_DROPOUT,
                 IMG_HEIGHT = settings.IMG_HEIGHT,
                 IMG_WIDTH = settings.IMG_WIDTH,
                 IMG_CHANNELS = settings.IMG_CHANNELS,
                 n_classes = settings.n_classes):
        
        self.features_map = features_map
        self.dropout = dropout
        self.dropout_rate = dropout_rate
        self.smooth = smooth
        self.learning_rate = learning_rate
        self.model_print = model_print
        self.use_dropout = use_dropout
        self.IMG_HEIGHT = IMG_HEIGHT
        self.IMG_WIDTH = IMG_WIDTH
        self.IMG_CHANNELS  =IMG_CHANNELS
        self.n_classes = n_classes

    def U_NET(self):
        inputs =  Input((self.IMG_HEIGHT,self.IMG_WIDTH,self.IMG_CHANNELS))
        
        dict_1 = dict(kernel_size=(3,3), activation='relu', padding='same',kernel_initializer='he_normal')
        dict_2 = dict(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        dict_trans = dict(kernel_size=(2,2), strides=(2,2),padding='same')
        
        c1=Conv2D(self.features_map, **dict_1)(inputs)
        if self.use_dropout:
            c1 = K.layers.SpatialDropout2D(self.dropout_rate)(c1)
        c1=Conv2D(self.features_map, **dict_1)(c1)
        p1=MaxPooling2D(pool_size=(2,2))(c1)
        
        c2=Conv2D(self.features_map*2, **dict_1)(p1)
        if self.use_dropout:
            c2 = K.layers.SpatialDropout2D(round(self.dropout_rate*2,2))(c2)
        c2=Conv2D(self.features_map*2, **dict_1)(c2) 
        p2=MaxPooling2D(pool_size=(2,2))(c2)

        c3=Conv2D(self.features_map*4, **dict_1)(p2)
        if self.use_dropout:
            c3 = K.layers.SpatialDropout2D(round(self.dropout_rate*2,2))(c3)
        c3=Conv2D(self.features_map*4, **dict_1)(c3) 
        p3=MaxPooling2D(pool_size=(2,2))(c3)

        c4=Conv2D(self.features_map*8, **dict_1)(p3)
        if self.use_dropout:
            c4 = K.layers.SpatialDropout2D(round(self.dropout_rate*3,2))(c4)
        c4=Conv2D(self.features_map*8, **dict_1)(c4) 
        p4=MaxPooling2D(pool_size=(2,2))(c4)
        
        c5=Conv2D(self.features_map*16,**dict_1)(p4)
        c5=Conv2D(self.features_map*16,**dict_1)(c5)
        
        t6=Conv2DTranspose(self.features_map*8, **dict_trans)(c5)
        m6=concatenate([t6,c4])
        
        
        c7=Conv2D(self.features_map*8, **dict_1)(m6)
        c7=Conv2D(self.features_map*8, **dict_1)(c7) 
        
        t7=Conv2DTranspose(self.features_map*4, **dict_trans)(c7)
        m7=concatenate([t7,c3])
        
        c8=Conv2D(self.features_map*4, **dict_1)(m7)
        c8=Conv2D(self.features_map*4, **dict_1)(c8) 
        
        t8=Conv2DTranspose(self.features_map*2, **dict_trans)(c8)
        m8=concatenate([t8,c2])
        
        c9=Conv2D(self.features_map*2,**dict_1)(m8)
        c9=Conv2D(self.features_map*2, **dict_1)(c9)
        
        
        t9=Conv2DTranspose(self.features_map, **dict_trans)(c9)
        m9=concatenate([t9,c1])
        
        c10=Conv2D(self.features_map,**dict_1)(m9)
        c10=Conv2D(self.features_map,**dict_1)(c10)
        
        outputs=Conv2D(self.n_classes,kernel_size=(1,1),activation='sigmoid')(c10)
        
        model = Model(inputs=[inputs],outputs=[outputs])
        model.compile(**dict_2)
        if self.model_print:
            model.summary()
        return model