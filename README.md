# Opetussovellus
Sovellus on yleinen opetuskäyttöön tarkoitettu sovellus, jonka avulla opettajat voivat luoda tehtäviä opiskelijoiden suoritettavaksi sekä seurata opiskelijoiden edistymistä.

## Keskeiset toiminnot

- Käyttäjä voi luoda tunnuksen ja kirjautua sisään opettajana tai opiskelijana.
  
- Opettajan roolissa käyttäjä voi luoda tehtäviä opiskelijoiden ratkaistavaksi.
- Opettaja voi myös muokata tai poistaa luomiaan tehtäviä.
- Opettaja näkee tilaston opiskelijoiden suorittamista tehtävistä.
  
- Opiskelija pystyy suorittamaan tehtäviä.
- Opiskelija näkee, mitä tehtäviä hän on suorittanut ja ovatko tehtävät ratkaistu oikein.

- Sekä opettajat että opiskelijat voivat lähettää viestejä keskustelualueella.
  
## Sovelluksen käynnistäminen
- Sovellus ei ole testattavissa Fly.iossa.
### Käynnistysohjeet 
- Kloonaa repositorio. Luo juurikansioon tiedosto .env, jonka sisällöksi
     - DATABASE_URL = (tietokannan paikallinen osoite)
     - SECRET_KEY = (salainen avain)
- Aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla
     - python3 -m venv venv
     - source venv/bin/activate
     - pip install -r ./requirements.txt
- Määritä tietokannan skeema komennolla
     - psql < schema.sql
- Käynnistä sovellus komennolla
     - flask run

## Välipalautus 3
Sovellukseen pystyy luomaan tunnuksen sekä kirjautumaa sisään ja ulos. Tunnusta luodessa tehdään käyttäjätunnus ja salasana, sekä valitaan rooliksi joko opettaja tai oppilas. Sisäänkirjautuneena sovelluksen etusivulla näkee listan luoduista tehtävistä. Tehtäväsivulle mennessä pystyy vastaamaan tehtävään oppilaan roolissa. Kun tehtävään on vastannut, näkyy oikea vastaus. Opettajan roolissa voi luoda uusia tehtäviä tai poistaa jo olemassa olevia. Tehtävää luodessa sille annetaan nimi, tehtävänanto sekä oikea vastaus. Lisäksi sovellukseen on lisätty viestiketju. Tällä hetkellä sovelluksesta puuttuu mahdollisuus nähdä tilastot suoritetuista tehtävistä. 



