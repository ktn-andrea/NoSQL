# -*- coding: windows-1250 -*-
import redis
import uuid
from _datetime import datetime

class UOsztaly():
    def __init__(self):
        
        redis_host=' . . . '
        redis_port=6379
        
        self.r=redis.Redis(host=redis_host, 
                           port=redis_port, 
                           decode_responses=True)
        
        
    def uj_sator(self, nev, ar):
        if self.r.hexists('h_satrak', nev):
            print("Mar van ilyen nevu sator:", nev)
        else:
            self.r.hset('h_satrak', nev, ar)
            print("Uj sator felveve:", nev, ar)
            
    def sator_ar_modosit(self, nev, ar):
        if self.r.hexists('h_satrak', nev):
            self.r.hset('h_satrak', nev, ar)
            print("Sator ara modositva:", nev, ar)
        else:
            print("Nincs ilyen nevu sator:", nev)
            
    def sator_jatek_felvesz(self, nev, jatek):
        if self.r.hexists('h_satrak', nev):
            self.r.rpush('jatekok_' + nev, jatek)
            print("Jatek felveve {} satorba: {}".format(nev, jatek))
        else:
            print("Nincs ilyen nevu sator.", nev)
            
    def sator_jatek_torol(self, nev, jatek):
        if self.r.hexists('h_satrak', nev):
            self.r.lrem('jatekok_' + nev, jatek, 1)
            print("Jatek torolve:", nev, jatek)
            
    def sator_lista(self):
        print('-'*30, "\nOsszes sator és bennuk levo jatekok:")
        for sator in self.r.hkeys('h_satrak'):
            sator_ar = self.r.hget('h_satrak', sator)
            jatekok = self.r.lrange('jatekok_'+sator, 0, -1)
            print(sator , ": ", sator_ar, jatekok)
        print('-'*30)
            
    def gyerek_adat_felvesz(self, telszam):
        azon = self.r.incr('gyerek_azon')
        print("Uj gyerek erkezett, sorszam:" , azon, "szulo telszama:", telszam)
        ido = datetime.now().strftime("%Y%m%d%H%M")
        p = self.r.pipeline()
        p.zadd('gyerekek', azon, ido)
        p.hset('gyerek_adatok', azon, telszam)
        p.execute()
        return azon
    
    def gyerek_adat_torol(self, azon):
        if self.r.hexists('gyerek_adatok', azon):
            p = self.r.pipeline()
            p.zrem('gyerekek', azon)
            p.hdel('gyerek_adatok', azon)
            p.execute()
            print("A sorrendben {}. erkezo gyerek adatait toroltuk.".format(azon))
        else:
            print("Nem talalhato ilyen sorszamu gyerek:", azon)
        
    def erkezesek_idorendben(self):
        print('-'*30)
        print("Gyermekek erkezese idorendben:")
        print('-'*20)
        for i in self.r.zrange('gyerekek', 0, -1, withscores=True):
            print("Gyerek sorszama:", i[0])
            print("Erkezes idopontja:", i[1])
            azon = i[0]
            print("Szulo telszam:" ,self.r.hget('gyerek_adatok', azon))
            print('-'*20)
        
    def szulo_adatok_felvetele(self, szulo_nev, telszam):
        if self.r.sismember('s_szulok', telszam):
            print("Mar van ilyen telefonszamhoz felveve adat.")
        else:
            self.r.sadd('s_szulok', telszam, szulo_nev)
            self.r.hmset('h_szulok_' + szulo_nev,{'nev:':szulo_nev, 'telszam':telszam} )
            print("Uj szulo adatai felveve:", szulo_nev, telszam)
            
    def szulok_listaja(self):
        print('-'*30)
        print("Az osszes szulo es adataik:")
        for i in self.r.smembers('s_szulok'):
            print(self.r.hgetall('h_szulok_'+i))
            
            
    def __generate_token(self):
        return str(uuid.uuid4())
    
    def uj_karszalag(self, azon):
        if self.r.hexists('gyerek_adatok', azon):
            tok = self.__generate_token()
            if self.r.hexists('h_tokenek', tok):
                print("Mar van ilyen sorszamu gyereken karszalag.")
            else:
                self.r.hset('h_tokenek', tok, azon)
                print("Karszalag kiadva:", tok)
                return tok
        else:
            print("Nem talalhato ilyen sorszamu gyerek.")
            
    def karszalag_torol(self, tok):
        a = self.r.hget('h_tokenek', tok)
        talalhato = False
        for i in self.r.hkeys('h_tokenek'):
            a2 = self.r.hget('h_tokenek', i)
            if a == a2:
                talalhato = True
                self.r.hdel('h_tokenek', i)
                print("Karszalag torolve:", tok)
                break
        if talalhato == False:
            print("Karszalag nem talalhato:", tok)
            
    def karszalag_ervenyes(self, tok):
        if self.r.hexists('h_tokenek', tok):
            print("Van ilyen karszalag regisztralva:", tok)
        else:
            print("Nincs ilyen karszalag regisztralva:", tok)

    def ervenyes_karszalagok(self):
        for i in self.r.hkeys('h_tokenek'):
            print("Rendezvenyen tartozkodik: ")
            print("karszalag:", i)
            sorszam = self.r.hget('h_tokenek', i)
            print("sorszam:", sorszam)
            print("telszam:", self.r.hget('gyerek_adatok', sorszam))
            
