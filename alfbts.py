import chardet,hashlib,io,numpy,os,random,re,threading,time,tkinter,turtle
from tkinter import filedialog,messagebox,ttk
from PIL import Image
pro_lst5=[0.006]*73+[0.06*i+0.006 for i in range(16)]+[1]
pro_lst4=[0.051]*8+[0.51*i+0.051 for i in range(4)]; tu_lst=[0.5,0.55,0.75,1]
dic=numpy.zeros(shape=(52,91,5,2)); tp=os.path
lst=numpy.zeros(shape=(38000,4),dtype=int); proes=numpy.zeros(38000)
name=['生命值','攻击力','防御力','生命值 ','攻击力 ','防御力 ',
      '元素充能效率','暴击率','暴击伤害','元素精通 ','治疗加成']
mnpro=[[[3],[1]],[[4],[1]],[[-1,6,9],[8,1,1]],[[-1,-2,9],[23,16,1]],
       [[-1,7,8,10,9],[33,5,5,5,2]]]
sipro=[4,4,4,6,6,6,4,3,3,4]; siupro=[0.7,0.8,0.9,1]
siup=[5.83,5.83,7.29,298.75,19.45,23.15,6.48,3.89,7.77,23.31]
knd=['生之花','死之羽','时之沙','空之杯','理之冠']; elmnkd='火水风雷草冰岩 '
libs=['pip','moment','chardet','csv','sqlite3','tkinter','jieba','os',
      'math','time','rich','PIL','requests','flask','django','jinja2',
      'scrapy','multiprocessing','turtle','threading','hashlib','sympy',
      'pygame','isort','cython','numpy','scipy','pandas','matplotlib',
      'cffi','ctypes','win32','win32ui','win32gui','algorithms']
hdnms={b'PNG':'.png',b'GIF8':'.gif',b'PDF':'.pdf',b'Rar!':'.rar',
       b'FLV':'.flv',b'BM':'.bmp',b'AVI LIST':'.avi',b'8BPS':'.psd',
       b'WAVEfmt':'.wav',b'MZ':'.exe',b'ftypmp':'.mp4',b'ftypM4':'.m4a',
       b'\xff\xd8\xff':'.jpg',b'\x49\x49\x2a\x00':'.tiff',b'\x1f\x8b':'.gz',
       b'PK\x03\x04':'.zip',b'7Z\xBC\xAF\x27':'.7z',b'\x49\x44\x33':'.mp3'}
icc=('r27l213br26l22r24l24l12l22r24l22r24l22el111l23br22l24l12l24er28r13br22'
     'l22r24l23r22r12l12l27l12l23r24l23r22r17r26l22l16r111r24l22r24l22l14r12'
     'l23r13l227el14l215br26l22l16l22el32r22bl23r22r13l12l25l16l25l12el27l17'
     'br12l12l22l12el28l11bl34r12l12l22r24r12l12l27l12l23r24r12l12l22r24l22e')
class Alfbts:
    def __init__(self):
        self.rt=tkinter.Tk(); self.adcon(); self.admnu(); self.prefn()
        self.rt.iconphoto(True,tkinter.PhotoImage(file='Na.png'))
        self.rt.title('自制小工具集合 By——红石社Deiloproxide')
        self.rt.geometry('960x540'); self.ico(); self.rt.mainloop()
    def adcon(self):
        self.ls=ttk.Treeview(self.rt,columns=('opt',),show='tree')
        self.slb=tkinter.Scrollbar(self.rt); self.cvs=tkinter.Canvas(self.rt)
        self.sc=turtle.TurtleScreen(self.cvs); self.tl=turtle.RawTurtle(self.sc)
        self.ls.column("#0",width=0,stretch=False)
        self.ls.column('opt',width=200,anchor='w')
        self.ls.config(yscrollcommand=self.slb.set)
        self.slb.config(command=self.ls.yview)
    def adfun(self,lbl,knd):
        mntmp=tkinter.Menu(self.mnu,tearoff=0)
        self.mnu.add_cascade(label=lbl,menu=mntmp)
        for i in knd: mntmp.add_command(label=i,command=knd[i])
    def admnu(self):
        self.clr={'black','red','green','yellow','blue','purple','cyan','grey','white'}
        self.funknd={
        '文件(F)':{'清空':self.clear,'图标':self.ico,'库检测':lambda: self.thr(self.lbdet),
            '退出':lambda: self.winqut(self.rt)},
        '算法(A)':{'同分异构体数量':lambda: self.thr(self.iso),
            '链表冒泡排序':lambda: self.thr(self.lnksrt),'最大环长度':lambda: self.thr(self.ring),
            '求解罗马数字':lambda: self.thr(self.rome)},
        '批处理(B)':{'补齐缺失后缀':lambda: self.thr(self.adlsnd),
            '图片颜色替换':lambda: self.thr(self.clrplc),'图片排序':lambda: self.thr(self.imgsrt),
            '图片加解密':lambda: self.thr(self.picpt),'生成组合字符':lambda: self.txmng(self.rndchr),
            '解unicode':lambda: self.txmng(self.ucd),'视频重命名':lambda: self.thr(self.vdornm)},
        '功能(T)':{'抽卡模拟器':self.conpuw,'圣遗物强化':self.itsth,'迷宫可视化':self.mazepl,
            '抽卡概率计算':lambda: self.thr(self.pulpro)}}
        self.mnu=tkinter.Menu(self.rt)
        for i in self.clr: self.ls.tag_configure(i,foreground=i)
        for i in self.funknd: self.adfun(i,self.funknd[i])
        self.rt.config(menu=self.mnu)
    def adlsnd(self):
        self.show(self.ls,'I.initialize','cyan')
        self.pth=self.dlg(0,'文件夹选择',('Text files','*.txt'))
        if not self.pth: return
        fnames=[i for i in os.listdir(self.pth) if tp.isfile(self.pnm(i))]
        names=[i for i in fnames if not tp.splitext(i)[1]]
        self.show(self.ls,'II.convert','cyan'); lnm=len(names)
        if names: self.pginit('查找添加缺失后缀',lnm)
        for i in range(lnm):
            nm=self.pnm(names[i]); fl=open(nm,'rb'); hd=fl.read(32); fl.close()
            for j in hdnms:
                if j in hd:
                    self.pgu(i+1,f"{name} -> {name+hdnms[j]}",'cyan')
                    os.rename(nm,nm+hdnms[j]); break
            else: self.pgu(i+1,f'unknown file type: {name}','red')
        self.show(self.ls,'successful!','red')
        self.rt.after(1000); self.winqut(self.pgm,ask=False)
    def adups(self,i,n):
        if i in self.ups: messagebox.showwarning('选择角色重复','请重新选择')
        else: self.ups[n]=i; self.show(self.et,f'角色{i}添加成功!','red')
        for i in self.ups:
            if not i: return
        self.btn1.config(state='normal'); self.btn2.config(state='normal')
    def clear(self): self.ls.delete(*self.ls.get_children())
    def clrplc(self):
        self.show(self.ls,'I.initialize','cyan')
        pnm=self.dlg(1,'图片文件选择',('All image files','*.*'))
        if not pnm: return
        pic=Image.open(pnm)
        fm=lambda cl: (int(cl[:2],16),int(cl[2:4],16),int(cl[4:],16))
        nclr=list(map(fm,self.lmd('输入多个被替换颜色(16进制表示)').split()))
        clr=fm(self.lmd('输入替换颜色(16进制表示)'))
        self.show(self.ls,'II.replace colors','cyan'); pix=numpy.array(pic)
        for i in nclr: alc=(pix[:,:,:3]==i).all(axis=-1); pix[alc,:3]=clr
        self.show(self.ls,'IV.save','cyan'); pic=Image.fromarray(pix)
        new=self.dlg(2,'图片文件保存',('Image files','*.png'))
        if not new: return
        if new.endswith('.png'): pic.save(new)
        else: pic.save(f'{new}.png')
        self.show(self.ls,'successful!','red')
    def conpuw(self):
        self.pu=tkinter.Toplevel(self.rt)
        self.pu.title('抽卡模拟器'); self.pu.geometry('400x450')
        self.pum=tkinter.Menu(self.pu); self.pu.config(menu=self.pum)
        self.ups5=tkinter.Menu(self.pum,tearoff=0)
        self.ups41=tkinter.Menu(self.pum,tearoff=0)
        self.ups42=tkinter.Menu(self.pum,tearoff=0)
        self.ups43=tkinter.Menu(self.pum,tearoff=0)
        self.pum.add_cascade(label='五星UP',menu=self.ups5)
        self.pum.add_cascade(label='四星UP1',menu=self.ups41)
        self.pum.add_cascade(label='四星UP2',menu=self.ups42)
        self.pum.add_cascade(label='四星UP3',menu=self.ups43)
        self.dtm={'ups5':None,'ups4':None,'fups5':None,
                  'wpns5':None,'wpns4':None,'wpns3':None}
        itm,litm,ctm,self.put5,self.put4,self.true_up5,self.true_up4=['']*100,0,'',0,0,0,0
        self.fu,self.ups=0,['']*4
        libf=open('pulchrlibs.txt','rb'); data=libf.read(); libf.close()
        enc=chardet.detect(data)['encoding']; libs=data.decode(enc).split('\r\n')
        for i in libs:
            if not ctm: ctm=i
            elif i in self.dtm: self.dtm[ctm]=itm[:litm]; litm=0; ctm=i
            else:
                for j in i.split():
                    if ctm=='ups5':
                        self.ups5.add_command(label=j,command=lambda j=j: self.adups(j,0))
                    elif ctm=='ups4':
                        self.ups41.add_command(label=j,command=lambda j=j: self.adups(j,1))
                        self.ups42.add_command(label=j,command=lambda j=j: self.adups(j,2))
                        self.ups43.add_command(label=j,command=lambda j=j: self.adups(j,3))
                    itm[litm]=j; litm+=1
        self.dtm[ctm]=itm[:litm]; self.lb=tkinter.Label(self.pu,text='祈愿结果:')
        self.et=ttk.Treeview(self.pu,columns=('opt',),show='tree')
        self.slet=tkinter.Scrollbar(self.pu); self.emp=tkinter.Frame(self.pu)
        self.btn1=tkinter.Button(self.emp,text='祈愿一次',command=lambda: self.pul(1))
        self.btn2=tkinter.Button(self.emp,text='祈愿十次',command=lambda: self.pul(10))
        self.btn3=tkinter.Button(self.emp,text='退出',command=lambda: self.winqut(self.pu))
        self.btn1.config(width=8,state='disabled')
        self.btn2.config(width=8,state='disabled')
        self.btn3.config(width=8)
        self.et.column("#0",width=0,stretch=False)
        self.et.column('opt',width=200,anchor='w')
        self.et.config(yscrollcommand=self.slet.set)
        self.slet.config(command=self.et.yview)
        for i in self.clr: self.et.tag_configure(i, foreground=i)
        self.slet.pack(side='right',fill='y'); self.lb.pack(expand=True)
        self.et.pack(fill='both',expand=True); self.emp.pack(fill='x',expand=True)
        self.btn1.pack(side='left',expand=True)
        self.btn2.pack(side='left',expand=True)
        self.btn3.pack(side='left',expand=True)
        self.pu.grab_set(); self.pu.wait_window()
    @staticmethod
    def dlg(n,tle,flt):
        if n==0: dl=filedialog.askdirectory(title=tle)
        elif n==1: dl=filedialog.askopenfilename(title=tle,filetypes=(flt,))
        else: dl=filedialog.asksaveasfilename(title=tle,filetypes=(flt,))
        return dl
    def gen(self):
        self.tl.reset(); self.tl.ht(); self.tl.speed(0); self.tl.penup()
        self.ln,self.wd=map(int,self.lmd('输入迷宫的长和宽').split())
        self.bx,self.by=map(int,self.lmd('输入迷宫起始点x,y').split())
        self.ex,self.ey=map(int,self.lmd('输入迷宫终点x,y').split())
        self.btn4.config(state='disabled')
        self.sz=min(200/self.ln,200/self.wd)
        self.maze=numpy.ones(shape=(self.ln*2+1,self.wd*2+1),dtype=int)
        for i in range(self.ln*2+1):
            for j in range(self.wd*2+1):
                if i in [0,self.ln*2] or j in [0,self.wd*2]: self.maze[i,j]=0
        self.mzshw(0,0,self.ln*2+1,self.wd*2+1,'#000000')
        self.mzshw(1,1,self.ln*2,self.wd*2,'#ffffff')
        stk,top=numpy.zeros(shape=(50,4),dtype=int),0
        stk[top]=[1,1,self.ln*2-1,self.wd*2-1]; top+=1
        while top>0:
            top-=1; lx,ly,rx,ry=stk[top]
            if rx-lx<2 or ry-ly<2: continue
            x=random.randint(lx+1,rx-1)//2*2; y=random.randint(ly+1,ry-1)//2*2
            stk[top]=[lx,y+1,x-1,ry]; top+=1; stk[top]=[lx,ly,x-1,y-1]; top+=1
            stk[top]=[x+1,ly,rx,y-1]; top+=1; stk[top]=[x+1,y+1,rx,ry]; top+=1
            for i in range(lx,rx+1): self.maze[i][y]=0
            for i in range(ly,ry+1): self.maze[x][i]=0
            self.mzshw(lx,y,rx+1,y+1,'#000000'); self.mzshw(x,ly,x+1,ry+1,'#000000')
            rtmp=[(random.randint(lx,x-1)//2*2+1,y),(random.randint(x+1,rx)//2*2+1,y),
                  (x,random.randint(ly,y-1)//2*2+1),(x,random.randint(y+1,ry)//2*2+1)]
            k=random.randrange(4)
            for i in range(4):
                if k-i:
                    self.maze[rtmp[i][0],rtmp[i][1]]=1
                    self.mzshw(rtmp[i][0],rtmp[i][1],rtmp[i][0]+1,rtmp[i][1]+1,'#ffffff')
        self.maze[self.bx*2-1,self.by*2-1]=1; self.maze[self.ex*2-1,self.ey*2-1]=2
        self.mzshw(self.bx*2-1,self.by*2-1,self.bx*2,self.by*2,'#22cefc')
        self.mzshw(self.ex*2-1,self.ey*2-1,self.ex*2,self.ey*2,'#00ff00')
        self.btn4.config(state='normal'); self.btn5.config(state='normal')
    def getit(self):
        self.sis,self.lvl,self.kd=[0]*4,[0]*5,random.randrange(5)
        self.mn=random.choices(mnpro[self.kd][0],weights=mnpro[self.kd][1])[0]
        if self.mn==-1: self.mn=random.randint(0,2)
        if self.mn==-2:
            self.mn=random.choice(elmnkd)
            if self.mn==' ': self.mn='物理'
            else: self.mn+='元素'
            self.mn+='伤害加成'
        else: self.mn=name[self.mn]
        self.sisl,self.nm=0,random.choices((3,4),weights=(4,1))[0]
        while self.sisl in range(self.nm):
            si=random.choices(range(len(sipro)),weights=sipro)[0]
            if si not in self.sis and name[si]!=self.mn:
                self.lvl[self.sisl]=siup[si]*random.choice(siupro)
                self.sis[self.sisl]=si; self.sisl+=1
        self.btn2.config(state='normal')
        self.et.delete(*self.et.get_children()); self.prit()
    def getvar(self):
        self.var=self.etr.get()
        if self.var: self.tmp.destroy()
    def ico(self):
        self.ls.pack_forget(); self.slb.pack_forget()
        self.cvs.pack(fill='both',expand=True)
        self.tl.ht(); self.tl.speed(0); self.tl.penup()
        self.tl.color('#22cefc'); i,j,cmd,dig=0,len(icc),int,'0'
        cmds={'b':lambda a: (self.tl.begin_fill(),self.tl.pendown()),
             'e':lambda a: (self.tl.end_fill(),self.tl.penup()),
             'l':lambda a: (self.tl.lt(int(a[0])*60),self.tl.fd(int(a[1:])*10)),
             'r':lambda a: (self.tl.rt(int(a[0])*60),self.tl.fd(int(a[1:])*10))}
        while i<j:
            if icc[i].isdigit(): dig+=icc[i]
            else: cmd(dig); dig,cmd='',cmds[icc[i]]
            i+=1
        cmd(dig); self.rt.after(1000); self.cvs.pack_forget(); self.tl.reset(); self.tl.ht()
        self.slb.pack(side='right',fill='y'); self.ls.pack(fill='both',expand=True)
    def imgsrt(self):
        self.show(self.ls,'I.initialize','cyan')
        self.pth=self.dlg(0,'文件夹选择',('Text files','*.txt'))
        if not self.pth: return
        self.show(self.ls,'II.image sort(maybe long time)','cyan')
        names=[i for i in os.listdir(self.pth) if i.lower().endswith('.png')]
        ln=len(names); lnr=range(ln); self.pginit('图片排序',ln)
        msg=lambda tx,x: self.pgu(x+1,f'已{tx}{x+1}/{len(names)}','cyan')
        pis=[[numpy.array(Image.open(self.pnm(names[i])))[:,:3],msg('转换',i)] for i in lnr]
        self.rt.after(1000); self.winqut(self.pgm,ask=False); self.pginit('图片排序',ln)
        sort=[[numpy.mean(pis[i][0]),names[i],msg('完成',i)] for i in lnr]
        self.rt.after(1000); self.winqut(self.pgm,ask=False)
        sort=sorted(sort,key=lambda i:i[0]); self.show(self.ls,'III.uniform','cyan')
        for i in lnr: os.rename(self.pnm(sort[i][1]),self.pnm(f'pix{i:04d}.png'))
        names=[i for i in os.listdir(self.pth) if i.lower().endswith('.png')]
        for i in lnr: os.rename(self.pnm(names[i]),self.pnm(f'pic{i:04d}.png'))
        self.show(self.ls,'successful!','red')
    def inp(self,st,tx,ab,tx1,tx2,cmd1,cmd2):
        self.tmp=tkinter.Toplevel(self.rt)
        self.tmp.title(''); self.tmp.geometry('220x100')
        self.lb=tkinter.Label(self.tmp,text=st)
        self.etr=tkinter.Entry(self.tmp); self.etr.insert('end',tx)
        self.emp=tkinter.Frame(self.tmp)
        self.btn1=tkinter.Button(self.emp,text=tx1,command=cmd1)
        self.btn2=tkinter.Button(self.emp,text=tx2,command=cmd2)
        self.btn1.config(width=10); self.btn2.config(width=10)
        self.lb.pack(expand=True)
        if ab: self.etr.pack(expand=True)
        self.emp.pack(fill='x',expand=True)
        self.btn1.pack(side='left',expand=True)
        self.btn2.pack(side='right',expand=True)
        self.tmp.grab_set(); self.tmp.wait_window()
        return self.var
    def iso(self):
        n=int(self.lmd('基团-CnH2n+1,输入n值'))
        hm,isol=numpy.zeros(n+1,dtype=int),1; hm[0]=1
        for i in range(n):
            b,c,res=0,0,0; a=i-2*c
            while c<=a:
                res+=hm[a]*hm[b]*hm[c]; a,b=a-1,b+1
                if a<b: c+=1; a,b=i-2*c,c
            hm[isol],isol=res,isol+1
        self.show(self.ls,f'{hm[n]}','green')
    def itsth(self):
        self.it=tkinter.Toplevel(self.rt)
        self.it.title('圣遗物强化'); self.it.geometry('400x450')
        self.lb=tkinter.Label(self.it,text='强化结果:')
        self.et=ttk.Treeview(self.it,columns=('opt',),show='tree')
        self.slet=tkinter.Scrollbar(self.it)
        self.emp=tkinter.Frame(self.it)
        self.btn1=tkinter.Button(self.emp,text='获取',command=self.getit)
        self.btn2=tkinter.Button(self.emp,text='强化',command=self.upgd)
        self.btn3=tkinter.Button(self.emp,text='退出',command=lambda: self.winqut(self.it))
        self.btn1.config(width=8)
        self.btn2.config(width=8,state='disabled')
        self.btn3.config(width=8)
        self.et.column("#0",width=0,stretch=False)
        self.et.column('opt',width=200,anchor='w')
        self.et.config(yscrollcommand=self.slet.set)
        self.slet.config(command=self.et.yview)
        for i in self.clr: self.et.tag_configure(i, foreground=i)
        self.slet.pack(side='right',fill='y'); self.lb.pack(expand=True)
        self.et.pack(fill='both',expand=True); self.emp.pack(fill='x',expand=True)
        self.btn1.pack(side='left',expand=True)
        self.btn2.pack(side='left',expand=True)
        self.btn3.pack(side='left',expand=True)
        self.it.grab_set(); self.it.wait_window()
    def lbdet(self):
        unl=[]
        for i in libs:
            try: exec(f'import {i}')
            except ModuleNotFoundError:
                self.show(self.ls,f'缺少{i}库','red')
                unl.append(i)
            else: self.show(self.ls,f'包含{i}库','green')
        if unl: self.show(self.ls,'建议使用pip安装以下库:','red')
        for i in unl: self.show(self.ls,i,'red')
    def lnksrt(self):
        arr,hd=eval(self.lmd('输入链表')),int(self.lmd('输入头地址')); lnkl,cur=0,hd
        while cur!=-1: lnkl+=1; cur=arr[cur][1]
        for i in range(lnkl-1,-1,-1):
            p,q=hd,-1; r=arr[p][1]
            for j in range(i):
                if arr[p][0]>arr[r][0]:
                    if q==-1: hd=r
                    else: arr[q][1]=r
                    arr[p][1],arr[r][1]=arr[r][1],p; p,r=r,p
                p,q,r=r,p,arr[r][1]
        self.show(self.ls,f'{arr},head={hd}','green')
    def mazepl(self):
        self.mz=tkinter.Toplevel(self.rt)
        self.mz.title('迷宫可视化'); self.mz.geometry('300x100')
        self.lb=tkinter.Label(self.mz,text='迷宫设置')
        self.emp=tkinter.Frame(self.mz)
        self.btn4=tkinter.Button(self.emp,text='生成',command=self.gen)
        self.btn5=tkinter.Button(self.emp,text='解',command=self.slv)
        self.btn6=tkinter.Button(self.emp,text='退出',command=lambda: self.winqut(self.mz))
        self.btn4.config(width=8)
        self.btn5.config(width=8,state='disabled')
        self.btn6.config(width=8)
        self.ls.pack_forget(); self.slb.pack_forget()
        self.cvs.pack(fill='both',expand=True);
        self.lb.pack(expand=True); self.emp.pack(fill='x',expand=True)
        self.btn4.pack(side='left',expand=True)
        self.btn5.pack(side='left',expand=True)
        self.btn6.pack(side='left',expand=True)
        self.mz.grab_set(); self.mz.wait_window()
        self.cvs.pack_forget(); self.tl.reset()
        self.slb.pack(side='right',fill='y')
        self.ls.pack(fill='both',expand=True)
    def mzshw(self,lx,ly,rx,ry,clr):
        self.tl.teleport((lx-self.ln)*self.sz+280,(ly-self.wd)*self.sz-135)
        self.tl.fillcolor(clr); self.tl.begin_fill()
        for i in range(2):
            self.tl.fd((rx-lx)*self.sz); self.tl.lt(90)
            self.tl.fd((ry-ly)*self.sz); self.tl.lt(90)
        self.tl.end_fill()
    def pginit(self,tx,tol):
        self.pgm=tkinter.Toplevel(self.rt); self.pgm.title(tx);
        self.pgm.geometry('400x250'); self.pgb=ttk.Progressbar(self.pgm)
        self.pgsb=tkinter.Scrollbar(self.pgm)
        self.pgt=ttk.Treeview(self.pgm,columns=('opt',),show='tree')
        self.pgt.column("#0",width=0,stretch=False)
        self.pgt.column('opt',width=200,anchor='w')
        self.pgt.config(yscrollcommand=self.pgsb.set)
        self.pgsb.config(command=self.pgt.yview)
        for i in self.clr: self.pgt.tag_configure(i,foreground=i)
        self.pgb['maximum']=tol; self.pgb.config(length=350); self.pgb.pack()
        self.pgsb.pack(side='right',fill='y'); self.pgt.pack(fill='both',expand=True)
    def pgu(self,num,tx,clr): self.pgb['value']=num; self.show(self.pgt,tx,clr)
    def picpt(self):
        self.show(self.ls,'I.open image','cyan')
        fl=self.dlg(1,'图片文件选择',('All image files','*.*'))
        if not fl: return
        pic=Image.open(fl); pix,h,w=numpy.array(pic),pic.height,pic.width
        self.show(self.ls,'II.gen hash mask','cyan'); ln=len(pix[0,0])
        licc,lictmp,hdgl,hsh=len(icc),0,64,hashlib.sha256()
        immsk=numpy.zeros_like(pix); self.show(self.ls,'III.image encrypt','cyan')
        self.pginit('图片加密',h)
        for i in range(h):
            for j in range(w):
                for k in range(ln):
                    if hdgl==64:
                        hdgl=0; hsh.update(icc[lictmp%licc].encode())
                        lictmp+=1; hdg=hsh.hexdigest()
                    immsk[i,j,k]=int(hdg[hdgl:hdgl+2],16); hdgl+=2
            self.pgu(i+1,f'已加密{i+1}/{h}','cyan')
        pic=Image.fromarray(numpy.bitwise_xor(pix,immsk))
        self.winqut(self.pgm,ask=False)
        self.show(self.ls,'IV.save','cyan')
        new=self.dlg(2,'图片文件保存',('Image files','.png'))
        if not new: return
        if new.endswith('.png'): pic.save(new)
        else: pic.save(f'{new}.png')
        self.show(self.ls,'successful!','red')
    def prefn(self):
        self.pnm=lambda fn: tp.join(self.pth,fn)
        self.scl=lambda: self.etr.selection_range(0,'end')
        self.tru=lambda: self.putvar(True)
        self.fls=lambda: self.putvar(False)
        self.lmd=lambda ch: self.inp(ch,'',True,'全选','确认',self.scl,self.getvar)
    def prit(self,st=[]):
        self.show(self.et,f'{knd[self.kd]}(+{self.lvl[4]})','cyan')
        self.show(self.et,self.mn,'blue')
        for i in range(self.sisl):
            nm=name[self.sis[i]]; clr='red' if i in st else 'green'
            if nm[-1]==' ':
                self.show(self.et,f'{nm[:-1]}+{round(self.lvl[i]+0.05,1)}',clr)
            else: self.show(self.et,f'{nm}+{round(self.lvl[i]+0.05,1)}%',clr)
        self.show(self.et,'','black')
    def pul(self,n):
        for i in range(n):
            ran,tup=random.random(),random.random()
            if ran<=pro_lst5[self.put5]:
                if self.true_up5: self.show(self.et,self.ups[0],'yellow'); self.true_up5=0
                elif tup<=tu_lst[self.fu]:
                    self.show(self.et,self.ups[0],'yellow'); self.true_up5,self.fu=0,0
                else:
                    it=random.choice(self.dtm['fups5']+self.dtm['wpns5'])
                    self.show(self.et,it,'yellow'); self.show(self.et,'歪','red')
                    self.true_up5,self.fu=1,self.fu+1
                self.put5,self.put4=0,self.put4+1
            elif ran<=pro_lst5[self.put5]+pro_lst4[self.put4]:
                if tup<=0.5 or self.true_up4:
                    self.show(self.et,random.choice(self.ups[1:]),'purple')
                    self.true_up4=0
                else:
                    it=random.choice(self.dtm['ups4']+self.dtm['wpns4'])
                    self.show(self.et,it,'purple'); self.true_up4=1
                self.put5,self.put4=self.put5+1,0
            else:
                self.show(self.et,random.choice(self.dtm['wpns3']),'blue')
                self.put5,self.put4=self.put5+1,self.put4+1
        self.show(self.et,f'垫{self.put5}发','cyan')
    def pulpro(self):
        global dic,lst; res=numpy.zeros(52,dtype=float); s=int(self.lmd('原石数'))
        pb=int(self.lmd('粉球数')); put=int(self.lmd('垫池数(0-89)'))
        fu,tu=int(self.lmd('已经连歪数')),int(self.lmd('是否大保底(0/1)'))
        _len,st,ed=0,0,50; pb+=s//160; lst[_len]=[0,put,fu,tu]
        proes[_len]=1; _len+=1; self.pginit('抽卡模拟',pb)
        for i in range(pb):
            for j in range(_len):
                ups,puts,false_up,true_up=lst[j]; pro=proes[j]
                ups=min(ups,50); pros=pro_lst5[puts]; tu_pro=tu_lst[false_up]
                dic[ups,puts+1,false_up,true_up]+=pro*(1-pros)
                if true_up: dic[ups+1,0,false_up,0]+=pro*pros
                else:
                    dic[ups,0,false_up+1,1]+=pro*pros*(1-tu_pro)
                    dic[ups+1,0,0,0]+=pro*pros*tu_pro
            _len=0
            for j in range(52):
                for t in range(90):
                    for p in range(4):
                        for k in range(2):
                            if dic[j,t,p,k]!=0:
                                lst[_len]=[j,t,p,k]; proes[_len]=dic[j,t,p,k]
                                _len+=1; dic[j,t,p,k]=0
            self.pgu(i+1,f'已完成{i+1}抽','cyan')
        for i in range(_len): res[lst[i,0]]+=proes[i]*100
        for i in range(ed+1):
            if res[i]>0.1: st=i; break
        for i in range(ed,0,-1):
            if res[i]<0.1: res[i-1]+=res[i]
            else: ed=i; break
        self.winqut(self.pgm,ask=False)
        self.show(self.ls,'UP数 概率','purple')
        for i in range(st,ed+1): self.show(self.ls,f'{i:>2d}{res[i]:7.2f}%','purple')
    def putvar(self,val): self.var=val; self.tmp.destroy()
    def ring(self):
        n=int(self.lmd('输入n值(对)')); m,flg=0,[1]*(2*n)
        for i in range(2*n):
            k,rngl=i,0
            while flg[k]: flg[k],rngl=0,rngl+1; k=k*2 if k<n else 2*(k-n)+1
            m=max(m,rngl)
        self.show(self.ls,f'{m}','green')
    def rndchr(self):
        n=int(self.inp('输入字符密度','',True,'全选','确认',self.scl,self.getvar))
        lst=list(range(768,880))+list(range(1155,1162))
        self.show(self.ls,'III.insert','cyan'); txt=self.istm.read(1)
        while txt:
            self.ostm.write(txt.encode('utf-8')); chs=map(chr,random.choices(lst,k=n))
            for i in chs: self.ostm.write(i.encode('utf-8'))
            txt=self.istm.read(1)
    def rome(self):
        ch=self.lmd('输入罗马数字'); num,stk,top=0,[0]*len(ch),0
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
             'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}
        for i in ch:
            while top>0 and dic[i]>stk[top-1]: top-=1; num-=stk[top]
            stk[top]=dic[i]; top+=1
        while top>0: top-=1; num+=stk[top]
        self.show(self.ls,f'{num}','green')
    def show(self,arg,st,cl):
        itm=arg.insert('','end',values=(st,),tags=(cl,)); arg.see(itm)
    def slv(self):
        self.btn4.config(state='disabled'); self.btn5.config(state='disabled')
        tmp=[[1,0],[-1,0],[0,1],[0,-1]]; stk,top=numpy.zeros(shape=(200,3),dtype=int),0
        f=lambda j: tmp[i][j]+(tmp[i][j]<0); g=lambda j: tmp[i][j]*2+1-(tmp[i][j]<0)
        stk[top]=[self.bx*2-1,self.by*2-1,0]; flg=False
        while top>=0:
            x,y,i=stk[top]; self.maze[x][y]=0
            if flg:
                self.mzshw(x+f(0),y+f(1),x+g(0),y+g(1),'#22cefc')
                top-=1; continue
            if i==4: top-=1; continue
            if not self.maze[x+tmp[i][0]][y+tmp[i][1]]: stk[top][2]=i+1; continue
            if self.maze[x+tmp[i][0]*2][y+tmp[i][1]*2]==2: flg=True; continue
            self.maze[x+tmp[i][0]][y+tmp[i][1]]=0
            self.mzshw(x+f(0),y+f(1),x+g(0),y+g(1),'#ff00ff')
            if not self.maze[x+tmp[i][0]*2][y+tmp[i][1]*2]: stk[top][2]=i+1; continue
            top+=1; stk[top]=[x+tmp[i][0]*2,y+tmp[i][1]*2,0]
        self.btn4.config(state='normal')
    @staticmethod
    def thr(fun): tsk=threading.Thread(target=fun); tsk.start()
    def txmng(self,fun):
        self.show(self.ls,'I.input','cyan'); self.istm=io.StringIO()
        if self.inp('打开方式','',False,'文本输入','文件打开',self.tru,self.fls):
            self.istm.write(self.lmd('输入你的文本'))
        else:
            fl=open(self.dlg(1,'文本文件选择',('All text files','*.*')),'rb')
            if not fl: return
            data=fl.read(1024); enc=chardet.detect(data)['encoding']
            fl.seek(0); data=fl.readline()
            while data: self.istm.write(data.decode(enc)); data=fl.readline()
        self.show(self.ls,'II.output settings','cyan')
        if self.inp('保存方式','',False,'文本输出','文件保存',self.tru,self.fls):
            self.ostm=io.BytesIO(); self.istm.seek(0);
            fun(); self.ostm.seek(0); val=self.ostm.getvalue().decode('utf-8')
            self.inp('生成结果',val,True,'全选','确认',self.scl,self.getvar)
        else:
            new=self.dlg(2,'文本文件保存',('All text files','*.*'))
            if not new: return
            self.ostm=io.FileIO(new,'w'); self.istm.seek(0); fun(); self.ostm.seek(0)
        self.istm.close(); self.ostm.close()
        self.show(self.ls,'successful!','red')
    def ucd(self):
        self.show(self.ls,'III.decode unicodes','cyan')
        txt,demux=self.istm.readline(),lambda i:chr(int(i.group(1),16))
        while txt:
            dectx=re.sub('\\\\u([0-9A-Fa-f]{4})',demux,txt)
            self.ostm.write(dectx.encode('utf-8')); txt=self.istm.readline()
    def upgd(self):
        self.lvl[4]+=4
        if self.lvl[4]==20: self.btn2.config(state='disabled')
        if self.sisl==3:
            while self.sisl!=4:
                si=random.choices(range(len(sipro)),weights=sipro)[0]
                if si not in self.sis and name[si]!=self.mn:
                    self.lvl[self.sisl]=siup[si]*random.choice(siupro)
                    self.sis[self.sisl]=si; self.sisl+=1
            self.prit(st=[3])
        else:
            up=random.randrange(4)
            self.lvl[up]+=siup[self.sis[up]]*random.choice(siupro)
            self.prit(st=[up])
    def vdornm(self):
        self.show(self.ls,'I.get movie folder','cyan')
        self.pth=self.dlg(0,'文件夹选择',('Text files','*.txt'))
        if not self.pth: return
        names=[i for i in os.listdir(self.pth) if i.lower().endswith('.mp4')]
        self.show(self.ls,'II.rename movies','cyan'); lnms=len(names)
        if names: self.pginit('视频重命名',lnms)
        for i in range(lnms):
            t=time.localtime(tp.getctime(self.pnm(names[i])))
            new=f'{time.strftime("%Y%m%d_%H%M%S",t)}A.mp4'
            self.pgu(i+1,f'{names[i]} -> {new}','cyan')
            os.rename(self.pnm(names[i]),self.pnm(new))
        self.rt.after(1000); self.winqut(self.pgm,ask=False)
        self.show(self.ls,'successful!','red')
    @staticmethod
    def winqut(tlk,ask=True):
        if not ask: tlk.destroy()
        elif messagebox.askokcancel('退出','确认退出?'): tlk.destroy()
if __name__=='__main__': alfbts=Alfbts()
