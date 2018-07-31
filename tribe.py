####################################################################################################
# Define decompose_video(). Default values below are from the sample test case.
# Will leave room to change bundle value/price
#i_comp = 3
#ii_comp = 5
#iii_comp = 9
#int_n = 13
#i_val = 570
#ii_val = 900
#iii_val = 1530
####################################################################################################
def decompose_video(int_n=13,i_comp=3,ii_comp=5,iii_comp=9,i_val=570,ii_val=900,iii_val=1530,media_type='VID'):

    out_decomposition=[]
    out_imperfect=[]
    remainder=int_n

    for i in range(0,int_n//i_comp + 1):
        for ii in range(0,(int_n-i_comp*i)//ii_comp + 1):
            for iii in range(0,(int_n - i*i_comp - ii*ii_comp)//iii_comp + 1):
                if(i*i_comp + ii * ii_comp + iii * iii_comp == int_n):
                    out_decomposition.append('%d %s $%.2f' % (int_n, media_type,i * i_val + ii * ii_val + iii * iii_val))
                    if(iii>0):
                        out_decomposition.append('\t%d x %d $%d' % (iii, iii_comp, iii_val))
                    if(ii>0):
                        out_decomposition.append('\t%d x %d $%d' % (ii, ii_comp, ii_val))
                    if(i>0):
                        out_decomposition.append('\t%d x %d $%d' % (i, i_comp, i_val))
                    return out_decomposition
                    #handle unbundled media
                elif(int_n - (i * i_comp + ii * ii_comp + iii * iii_comp ) < remainder ):
                    remainder = int_n - (i * i_comp + ii * ii_comp + iii * iii_comp )
                    out_imperfect=[]
                    out_imperfect.append('%d %s $%.2f' % (int_n, media_type,i * i_val + ii * ii_val + iii * iii_val))
                    if(iii>0):
                        out_imperfect.append('\t%d x %d $%d' % (iii,iii_comp, iii_val))
                    if(ii>0):
                        out_imperfect.append('\t%d x %d $%d' % (ii,ii_comp, ii_val))                        
                    if(i>0):
                        out_imperfect.append('\t%d x %d $%d' % (i,i_comp, i_val))
                    out_imperfect.append('\t%d x 0 $0 (unbundled)' % (remainder))
    return out_imperfect                

####################################################################################################
# Define decompose_audio(). Default values below are from the sample test case.
# Will reuse decompose_video method
# i_comp = 3
# ii_comp = 6
# iii_comp = 9
# int_n = 15
# i_val = 427.50
# ii_val = 810
# iii_val = 1147.5
#     out_decomposition=[]
#     out_imperfect=[]
#     remainder=int_n
# 
#     for i in range(0, int_n // i_comp + 1):
#         for ii in range(0, (int_n - i_comp * i) // ii_comp + 1):
#             for iii in range(0, (int_n - i * i_comp - ii * ii_comp) // iii_comp + 1):
#                 if (i * i_comp + ii * ii_comp + iii * iii_comp == int_n):
#                     out_decomposition.append('%d %s $%.2f' % (int_n, media_type,i * i_val + ii * ii_val + iii * iii_val))
#                     if(iii>0):
#                         out_decomposition.append('\t%d x %d $%d' % (iii, iii_comp, iii_val))
#                     if(ii>0):
#                         out_decomposition.append('\t%d x %d $%d' % (ii, ii_comp, ii_val))
#                     if(i>0):
#                         out_decomposition.append('\t%d x %d $%d' % (i, i_comp, i_val))
#                     return out_decomposition

####################################################################################################
def decompose_audio(int_n=15,i_comp=3,ii_comp=6,iii_comp=9,i_val=427.50,ii_val=810,iii_val=1147.5,media_type='FLAC'):
    return decompose_video(int_n,i_comp,ii_comp,iii_comp,i_val,ii_val,iii_val,media_type)


####################################################################################################
# Define decompose_image(). Default values below are from the sample test case.
# Will leave room to change bundle value/price
#i_comp = 5
#ii_comp = 10
#int_n = 10
#i_val = 450
#ii_val = 800
####################################################################################################
def decompose_image(int_n=10,i_comp=5,ii_comp=10,i_val=450,ii_val=800,media_type='IMG'):

    out_decomposition=[]
    out_imperfect=[]
    remainder=int_n
    
    for i in range(0, int_n // i_comp + 1):
        for ii in range(0, (int_n - i_comp * i) // ii_comp + 1):
            if (i * i_comp + ii * ii_comp == int_n):
                out_decomposition.append('%d %s $%.2f' % (int_n,media_type,i*i_val+ii*ii_val))
                
                if(ii>0):
                    out_decomposition.append('\t%d x %d $%d' % (ii,ii_comp, ii_val))
                if(i>0):
                    out_decomposition.append('\t%d x %d $%d' % (i,i_comp, i_val))
                return out_decomposition
            
            elif(int_n - (i * i_comp + ii * ii_comp ) < remainder ):
                remainder = int_n - (i * i_comp + ii * ii_comp )
                out_imperfect=[]
                out_imperfect.append('%d %s $%.2f' % (int_n,media_type,i*i_val+ii*ii_val))
                if(ii>0):
                    out_imperfect.append('\t%d x %d $%d' % (ii,ii_comp, ii_val))
                if(i>0):
                    out_imperfect.append('\t%d x %d $%d' % (i,i_comp, i_val))
                out_imperfect.append('\t%d x 0 $0 (unbundled)' % (remainder))
                 
    return out_imperfect                

####################################################################################################
# Define extract_breakdown(). Get breakdown from one row string input
# test_input = '10 IMG 15 FLAC 13 VID'
####################################################################################################
def extract_breakdown(input_string='10 IMG 15 FLAC 13 VID'):
    input_list = input_string.split()
    output_val=[]
    while input_list:
        count = int(input_list.pop(0))
        media_type = input_list.pop(0)
        if (media_type == 'IMG'):
            output_val+= decompose_image(count)
        elif (media_type == 'FLAC'):
            output_val+= decompose_audio(count)
        elif (media_type == 'VID'):
            output_val+= decompose_video(count)
        else:
            output_val+= '%d %s INVALID MEDIA TYPE' % (count,media_type)
    return output_val
            
                