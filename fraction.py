# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
data = np.genfromtxt('statpol.dat',skip_header=1)


# %%
time = data[:,0]


# %%
def Block_Average(data,Max_block_Size=2):
    block_Mean = np.zeros(Max_block_Size)
    block_Var = np.zeros(Max_block_Size)
    block_sig = np.zeros(Max_block_Size)
    block_Err = np.zeros(Max_block_Size)
    Size = np.arange(1,Max_block_Size+1)
    for block_Size in Size:
        Nb = int(len(data)/block_Size)
        b_mean = np.zeros(Nb)
        for j in range(1,Nb+1):
            ibeg = (j-1) * block_Size
            iend = ibeg + block_Size
            b_mean[j-1] = np.mean(data[ibeg:iend])
        block_Mean[block_Size-1] = np.mean(b_mean)
        block_Var[block_Size-1] = np.var(b_mean)/(Nb-1)
        block_sig[block_Size-1] = np.sqrt(block_Var[block_Size-1])
        block_Err[block_Size-1] = block_sig[block_Size-1]/np.sqrt(Nb)
    return Size,block_Mean,block_sig,block_Err


# %%
b_frac = np.zeros(len(time)) #bridge
l_frac = np.zeros(len(time)) #loop
f_frac = np.zeros(len(time)) #free
d_frac = np.zeros(len(time)) #dangle
for i in range(0,len(time)):
    for j in range(1,321):
        if data[i,j] == 0:
            f_frac[i] = f_frac[i]+1
        if data[i,j]==3:
            b_frac[i] = b_frac[i]+1
        if data[i,j]==2:
            l_frac[i] = l_frac[i]+1
        if data[i,j]==1:
            d_frac[i] = d_frac[i]+1 
b_frac = b_frac/320
l_frac = l_frac/320
f_frac = f_frac/320
d_frac = d_frac/320     


# %%
bsize,b_m,b_s,b_e = Block_Average(b_frac,500)
dsize,d_m,d_s,d_e = Block_Average(d_frac,500)
fsize,f_m,f_s,f_e = Block_Average(f_frac,500)
lsize,l_m,l_s,l_e = Block_Average(l_frac,500)
print("Bridge: ",b_m[-1],' +- ',b_s[-1])
print("Loop: ",l_m[-1],' +- ',l_s[-1])
print("Free: ",f_m[-1],' +- ',f_s[-1])
print("Dangle: ",d_m[-1],' +- ',d_s[-1])


# %%
f = open('frac.dat','w')
print("Bridge:\n",file = f)
print(b_m[-1] , " +- ", b_s[-1],"\n",file = f)
print("Loop:\n",file = f)
print(l_m[-1] , " +- ", l_s[-1],"\n",file = f)
print("Free:\n",file = f)
print(f_m[-1] , " +- ", f_s[-1],"\n",file = f)
print("Dangle:\n",file = f)
print(d_m[-1] , " +- ", d_s[-1],"\n",file = f)
f.close()


# %%



