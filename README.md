# Opetussovellus
Sovellus on yleinen opetuskäyttöön tarkoitettu sovellus, jonka avulla opettajat voivat luoda tehtäviä opiskelijoiden suoritettavaksi sekä seurata opiskelijoiden edistymistä.

## Keskeiset toiminnot

- Käyttäjä voi luoda tunnuksen ja kirjautua sisään opettajana tai opiskelijana.
  
- Opettajan roolissa käyttäjä voi luoda kurssialueita, joihin hän voi lisätä ohjeita tai viestejä opiskelijoille sekä tehtäviä opiskelijoiden ratkaistavaksi.
- Opettaja voi myös muokata tai poistaa luomiaan tehtäviä tai kurssialueita.
- Opettaja näkee kurssille liittyneet opiskelijat ja tilaston opiskelijoiden suorittamista tehtävistä.
  
- Opiskelija voi liittyä eri kurssialueille.
- Liityttyään kurssille opiskelija näkee opettajan viestit ja pystyy suorittamaan tehtäviä.
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
 
## Välipalautus 2
Tällä hetkellä sovellukseen pystyy luomaan tunnuksen sekä kirjautumaan sisään ja ulos. Tunnusta luodessa tehdään käyttäjätunnus ja salasana, sekä valitaan rooliksi joko opettaja tai oppilas.
Sisäänkirjautuneena sovelluksen etusivulla näkee listan luoduista kursseista. Opettajan roolissa voi lisäksi luoda uuden kurssialueen tai poistaa jo olemassa olevan kurssialueen.
Opettajan roolissa kurssialueella näkyvät toiminnot "Lisää viesti tai ilmoitus" sekä "Lisää tehtävä". En ole kuitenkaan ehtinyt toteuttaa näitä toimintoja, joten tällä hetkellä linkit johtavat takaisin etusivulle.


