sigrity::open document {E:/Share/VakulabharanamX/pkg_and_brd_files/pkg_file/dg256eu_ww45p3_pisimulation.tgz} {!}
sigrity::import stackup {C:\Users\vakulabx\Desktop\StackUp.csv} {!}
sigrity::save {!} 
sigrity::close document {!} 
sigrity::open document {E:/Share/VakulabharanamX/pkg_and_brd_files/brd_file/M52606-001_brd/M52606-001.brd} {!}
sigrity::import PKG -SPDFile {E:/Share/VakulabharanamX/pkg_and_brd_files/pkg_file/dg256eu_ww45p3_pisimulation.spd} -OldCkt {BRDU1} -NewCkt {PKGA1} -method {SolderBall} -MatchSel {InheritPkg} -unit {mm} -height {4.7264e-02} -radius {2.4498e-02} -Prefix -ApplyTo {PKG&PCB} {!}
Sigrity::save {!}
Sigrity::Venkatesh {!}
Sigrity::Venkatesh ...
