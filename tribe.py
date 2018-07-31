
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
                
            
        