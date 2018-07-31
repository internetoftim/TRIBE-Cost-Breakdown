def decompose_video(int_n=13,i_comp=3,ii_comp=5,iii_comp=9,i_val=570,ii_val=900,iii_val=1530,media_type='VID'):
#     i_comp = 3
#     ii_comp = 5
#     iii_comp = 9
#     int_n = 13
#     i_val = 570
#     ii_val = 900
#     iii_val = 1530
    out_decomposition=[]
    for i in range(0, int_n // i_comp + 1):
        for ii in range(0, (int_n - i_comp * i) // ii_comp + 1):
            for iii in range(0, (int_n - i * i_comp - ii * ii_comp) // iii_comp + 1):
                if (i * i_comp + ii * ii_comp + iii * iii_comp == int_n):
                    out_decomposition.append('%d %s $%d' % (int_n, media_type,i * i_val + ii * ii_val + iii * iii_val))
                    if(iii>0):
                        
                        out_decomposition.append('%d x $%d' % (iii, iii_comp))
                    if(ii>0):
                        out_decomposition.append('%d x $%d' % (ii, ii_comp))
                    if(i>0):
                        out_decomposition.append('%d x $%d' % (i, i_comp))
                    return out_decomposition

def decompose_image(int_n=10,i_comp=5,ii_comp=10,i_val=450,ii_val=800,media_type='IMG'):
#     i_comp = 5
#     ii_comp = 10
    # int_n = 10
#     i_val=450
#     ii_val=800
    out_decomposition = []
    for i in range(0, int_n // i_comp + 1):
        for ii in range(0, (int_n - i_comp * i) // ii_comp + 1):
            if (i * i_comp + ii * ii_comp == int_n):
#                 print('%d MEDIATYPE $%d' % (int_n, i * i_val + ii * ii_val))
#                 print('%d x $%d' % (ii, ii_comp))
#                 print('%d x $%d' % (i, i_comp))
                out_decomposition.append('%d %s $%d' % (int_n,media_type,i*i_val+ii*ii_val))
                
                if(ii>0):
                    out_decomposition.append('%d x $%d' % (ii,ii_comp))
                if(i>0):
                    out_decomposition.append('%d x $%d' % (i,i_comp))
                return out_decomposition
                
            
        
        
            
                