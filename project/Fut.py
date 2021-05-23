# -*- coding: windows-1250 -*-
from Osztaly import UOsztaly

rf = UOsztaly()



rf.uj_sator('tarsasjatekozos', 1500)
rf.sator_jatek_felvesz('tarsasjatekozos', 'uno_kartya')
rf.sator_jatek_felvesz('tarsasjatekozos', 'uno_kartya')
rf.sator_jatek_felvesz('tarsasjatekozos', 'monopoly_tarsas')
rf.sator_lista()

rf.sator_ar_modosit('meseolvaso', 1000)
rf.uj_sator('meseolvaso', 900)
rf.sator_ar_modosit('meseolvaso', 1000)
rf.sator_jatek_felvesz('meseolvaso', 'Vuk_konyv')
rf.sator_jatek_felvesz('meseolvaso', 'A_kis_herceg_konyv')

rf.uj_sator('ugralovar', 2000)
rf.sator_jatek_felvesz('ugralovar', 'hercegno_var')
rf.sator_jatek_felvesz('ugralovar', 'gorilla_var')
rf.sator_lista()

rf.sator_jatek_felvesz('meseolvaso', 'Csipkerozsika_konyv')
rf.sator_jatek_torol('meseolvaso', 'Csipkerozsika_konyv')
rf.sator_lista()



rf.gyerek_adat_felvesz("06-20-123")
rf.gyerek_adat_felvesz("06-20-456")
rf.gyerek_adat_felvesz("06-30-789")

rf.gyerek_adat_torol(1)

rf.erkezesek_idorendben()

rf.szulo_adatok_felvetele('edith_piaf', "06-20-123")
rf.szulo_adatok_felvetele('liszt_ferenc', "06-20-456")
rf.szulo_adatok_felvetele('bartok_bela', "06-30-789")
rf.szulok_listaja()



rf.erkezesek_idorendben()
rf.ervenyes_karszalagok()

rf.uj_karszalag(1)      # adatai torolve
rf.uj_karszalag(2)
rf.uj_karszalag(3)
rf.uj_karszalag(-1222)  # nincs 


rf.ervenyes_karszalagok()


rf.ervenyes_karszalagok()
rf.karszalag_ervenyes("494fa055-d17c-4a22-b5e6-68f1ff848ad8")
rf.karszalag_ervenyes("450271bd-a51b-49c5-8ae8-efa984235873")
rf.karszalag_ervenyes("valami")     # nincs 
rf.karszalag_torol("gorogdinnye")   # nincs 
rf.karszalag_torol("450271bd-a51b-49c5-8ae8-efa984235873")
rf.ervenyes_karszalagok()

