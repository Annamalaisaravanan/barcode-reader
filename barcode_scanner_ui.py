# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:41:03 2022

@author: Annamalai
"""

import streamlit as st
import cv2
from PIL import Image
from pyzbar.pyzbar import decode


st.set_page_config(page_title="Brand Identification App")
st.header("Brand Identification App")

select = st.sidebar.selectbox('Select',['','Barcode generator','Barcode reader'])

if select == 'Barcode reader':
                    dataset_load=st.file_uploader('Upload a barcode',type=['.png','.jpeg','.jpg'])
                    
                    product_dict = {
                                    "b'8901491503044'":{'name':'lays(tomato)','price':10,'quantity':65},
                                    "b'8901491503037'":{'name':'lays(green)','price':10,'quantity':65},
                                    "b'8901063029231'":{'name':'jimjam','price':20,'quantity':250},
                                    "b'8901063035102'":{'name':'milk bikies','price':25,'quantity':500}
                                   }
                    
                    def load_image(image_file):
                    	img = Image.open(image_file)
                    	return img
                    
                    
                    def BarcodeReader(image):
                    
                        # read the image in numpy array using cv2
                        #img = cv2.imread(image)
                    
                        # Decode the barcode image
                        detectedBarcodes = decode(image)
                      
                        # If not detected then print the message
                        if not detectedBarcodes:
                            st.write("Barcode Not Detected or your barcode is blank/corrupted!")
                        else:
                    
                            for barcode in detectedBarcodes:
                    
                                
                                (x, y, w, h) = barcode.rect
                                
                                if barcode.data!="":
                    
                                        # Print the barcode data
                                        #print(barcode.data)
                                        #print(f"{str(barcode.data)}")
                                        try:
                                                st.write(product_dict[f"{str(barcode.data)}"])
                                                print(barcode.type)
                                        
                                        except KeyError:
                                              st.write("The product is not found in the inventory ", barcode.data)
                                        
                    
                                        
                                                
                                        
                    
                        
                    if dataset_load:
                        
                           print("File Uploaded")
                           
                           BarcodeReader(load_image(dataset_load))
elif select == 'Barcode generator':
       st.write("That feature is still in progress.")