[33mcommit a35e628271b3e035b4f7cc657e959dd38d5cc212[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: JustinLungu <iustinl113@gmail.com>
Date:   Sat Sep 7 18:53:26 2024 +0200

    comments + add linemod to gitignore

[33mcommit 3b14f8ef5a7015c6ecfc52fb4b855a5b276801fc[m
Author: JustinLungu <iustinl113@gmail.com>
Date:   Sat Sep 7 17:52:53 2024 +0200

    echo project_dir

[33mcommit f0eb27b26da9923cb038e547070c1fe754fb6243[m
Author: JustinLungu <iustinl113@gmail.com>
Date:   Sat Sep 7 17:14:29 2024 +0200

    depth maps in mini-batches for GPU optimization (8GiB)

[33mcommit dc7568e3c9cf6b188e9cee7866538462e9856c81[m
Author: JustinLungu <iustinl113@gmail.com>
Date:   Tue Sep 3 11:34:42 2024 +0200

    kinect driller path change

[33mcommit 0f43dc7c6630c896a21b65e648efe68db83ec4ba[m
Author: JustinLungu <iustinl113@gmail.com>
Date:   Tue Sep 3 11:33:23 2024 +0200

    bind mount for dev changes

[33mcommit 7b1be7bd4060de39c568ab9c40b85de1e543da87[m
Author: JustinLungu <iustinl113@gmail.com>
Date:   Tue Sep 3 11:31:42 2024 +0200

    env setup change for my gpu

[33mcommit 79cdef9f02948aeb19cd001861bdb2aadbc65a8b[m
Author: JustinLungu <iustinl113@gmail.com>
Date:   Tue Sep 3 11:30:57 2024 +0200

    env setup change for my gpu

[33mcommit cd3ca4bc080529c53d5e5235212ca476d82bccf7[m
Author: Bowen Wen <365867978@qq.com>
Date:   Sat Aug 17 22:24:06 2024 -0700

    Update readme.md

[33mcommit 28d34ae01883c00b6565b9fe38271dc1f0f69797[m
Merge: 8df6f5d ae8dd0c
Author: Bowen <365867978@qq.com>
Date:   Thu Aug 15 22:48:47 2024 -0700

    Merge branch 'main' of https://github.com/NVlabs/FoundationPose into main

[33mcommit 8df6f5d79fc575a6a3dca7b43245d7e9df6ecd3b[m
Author: Bowen <365867978@qq.com>
Date:   Thu Aug 15 22:48:45 2024 -0700

    change zmin clip to 0.001

[33mcommit ae8dd0c0108113cac2c6ea0490381de495f39b77[m
Author: Bowen Wen <365867978@qq.com>
Date:   Fri Jul 19 14:15:23 2024 -0700

    Update readme.md

[33mcommit 91de95939a0c37757fc789b4041db37373838117[m
Merge: 99b82aa b07986c
Author: Bowen <365867978@qq.com>
Date:   Sun Jun 23 22:16:01 2024 -0700

    Merge branch 'main' of https://github.com/NVlabs/FoundationPose into main

[33mcommit 99b82aa2dae48a306df4fc1e6eb653e69f160e26[m
Author: Bowen <365867978@qq.com>
Date:   Sun Jun 23 22:15:58 2024 -0700

    update readme

[33mcommit b07986c8bed9784cf46740e32e520272e4e0af11[m
Merge: 92cd50a 94a6e8f
Author: Bowen Wen <365867978@qq.com>
Date:   Sun Jun 9 13:30:25 2024 -0400

    Merge pull request #153 from MichaelRazum/patch-1
    
    Update build_all.sh

[33mcommit 92cd50a59f2391167feffd170902e543a2d07010[m
Author: Bowen Wen <365867978@qq.com>
Date:   Sun Jun 9 10:18:53 2024 -0700

    Update readme.md

[33mcommit 94a6e8fc0a9821c46a6adcd31a22a8d9a35a85bb[m
Author: Michael Razum <michael.razoumovitch@gmail.com>
Date:   Wed Jun 5 09:12:00 2024 +0200

    Update build_all.sh
    
    When using different python version, for example with pyenv, cmake should bind to the currently used python version

[33mcommit fc034ecc98c205d324f869f3fdf11fe37ff9e2de[m
Author: Bowen <365867978@qq.com>
Date:   Sun Jun 2 17:28:00 2024 -0700

    update readme

[33mcommit 703035974a441f04ee12758f10003da97c1c0c61[m
Merge: 69db1c3 a2e4f4f
Author: Bowen Wen <365867978@qq.com>
Date:   Fri May 17 18:02:20 2024 -0400

    Merge pull request #126 from justin871030/patch-1
    
    Fix the command for conda environment in readme.md

[33mcommit a2e4f4f970d58d40e278f83c81b0bd5fa82b38b2[m
Author: double_fong <33437552+justin871030@users.noreply.github.com>
Date:   Tue May 14 11:55:08 2024 -0700

    Fix the command for conda environment in readme.md

[33mcommit 69db1c3d3555a6f4176a36bcd662dcc72a057903[m
Merge: fce37c8 88177b7
Author: Bowen Wen <365867978@qq.com>
Date:   Fri May 10 12:48:06 2024 -0400

    Merge pull request #113 from ShangQingLiu/main
    
    Optimize the eigen install under --user level

[33mcommit 88177b74208420332d43b10f2409f10b5e068a06[m
Author: Shang-Ching Liu <shangching@live.com>
Date:   Wed May 8 17:36:24 2024 +0200

    Optimize the eigen install under --user level
    
    Due to the sudoer issue the original eigen install steps is not good for
    public server, so I purpose a better solution.

[33mcommit fce37c86be33ee49cf0b46ee29ed26d613521d6d[m
Author: Bowen <365867978@qq.com>
Date:   Thu Apr 25 13:44:50 2024 -0700

    update

[33mcommit a0142aa4fe907056134115b8e3e31259425bd492[m
Author: Bowen <365867978@qq.com>
Date:   Thu Apr 25 10:58:46 2024 -0700

    run_demo change save path

[33mcommit 8395bd84adb0bfc3209cb9409e475cd1b51fc17b[m
Author: Bowen <365867978@qq.com>
Date:   Mon Apr 15 12:33:39 2024 -0700

    update docker/run_container.sh

[33mcommit 97095afa5f92be7cbe584fe3254d682943173947[m
Author: Bowen <365867978@qq.com>
Date:   Thu Apr 4 11:18:13 2024 -0700

    update readme

[33mcommit 11483f16fcf334c2dc10fbbda6aa098908a6f25a[m
Author: Bowen <365867978@qq.com>
Date:   Thu Apr 4 10:11:29 2024 -0700

    run_linemod.py fix bug of primitive mesh

[33mcommit 7b484cf03436b9bb6038768e6edd4bc06d759513[m
Author: Bowen <365867978@qq.com>
Date:   Wed Apr 3 16:29:13 2024 -0700

    update

[33mcommit fd5502b9643797638e4dde148339493d1ae8d7e4[m
Author: Bowen <365867978@qq.com>
Date:   Fri Mar 29 12:02:26 2024 -0700

    update readme

[33mcommit b753972d1f64561f9e33a44d25cb7382f69e7a7b[m
Author: Bowen <365867978@qq.com>
Date:   Fri Mar 29 11:56:46 2024 -0700

    remove unneeded package

[33mcommit ae68ee4224dbde08f6b6c0c6b029c9ae61c4ebe3[m
Merge: a630316 8c75f0d
Author: Bowen Wen <365867978@qq.com>
Date:   Fri Mar 29 11:54:50 2024 -0700

    Merge pull request #12 from gobanana520/main
    
    update conda env setup

[33mcommit 8c75f0d6faacd79ec0d33f8f6d730dd5f612c128[m
Author: Jikai Wang <jikai.wang@utdallas.edu>
Date:   Fri Mar 29 12:24:23 2024 -0500

    clean requirements.txt

[33mcommit 14f3e3f10d967faf66879f9224c44029690c9ba7[m
Author: Jikai Wang <jikai.wang@utdallas.edu>
Date:   Fri Mar 29 12:23:48 2024 -0500

    fix error in  build_all_conda.sh

[33mcommit 44456bc37c03c04a98c6636276bb6a8622f0aded[m
Author: Jikai Wang <jikai.wang@utdallas.edu>
Date:   Fri Mar 29 12:11:20 2024 -0500

    update conda env setup:

[33mcommit a630316cac631d5ad6080f97c7829ca88aaf3813[m
Author: Bowen Wen <365867978@qq.com>
Date:   Wed Mar 27 18:34:23 2024 -0700

    Update readme.md

[33mcommit 5f9db230f214bee4354120b1c5f88956691630f3[m
Author: Bowen Wen <365867978@qq.com>
Date:   Wed Mar 27 18:27:26 2024 -0700

    Update readme.md

[33mcommit ef23c3b4119980909ca4dcd557eeccae813f99e6[m
Author: noone <365867978@qq.com>
Date:   Thu Apr 27 23:39:09 2023 -0700

    first, 0daf657eaf571d82b29c11f2ecced297d138c4cd
