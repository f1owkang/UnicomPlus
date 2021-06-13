# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/root/UnicomDevelop'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
			 

def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))

    return extra_datas

# append the 'TaskList' dir
a.datas += extra_datas('TaskList')    
			 
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

			 
exe = EXE(pyz,
          a.scripts,
          a.binaries,                          
          a.zipfiles,                          
          a.datas,                             
          [],
          exclude_binaries=False,  
          name='UnicomPlus',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)
