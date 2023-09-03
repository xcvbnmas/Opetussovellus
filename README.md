# Opetussovellus
Sovellus on yleinen opetuskäyttöön tarkoitettu sovellus, jonka avulla opettajat voivat luoda tehtäviä opiskelijoiden suoritettavaksi.

## Keskeiset toiminnot

- Käyttäjä voi luoda tunnuksen ja kirjautua sisään opettajana tai opiskelijana.

### Opettajan roolissa
  
- Opettajan roolissa käyttäjä voi luoda tehtäviä opiskelijoiden ratkaistavaksi. Opettaja voi myös poistaa luomiaan tehtäviä.
- Tehtävälle annetaan nimi, tehtävänanto sekä mallivastaus. 
- Tehtävien lisäksi opettaja voi lisätä ilmoituksia sovelluksen etusivulle. 

### Opiskelijan roolissa
  
- Opiskelija pystyy suorittamaan tehtäviä ja näkee ilmoitukset etusivulla.
- Opiskelija suorittaa tehtävän kirjoittamalla vastauksen tekstilaatikkoon.
- Lähetettyään tehtävään vastauksen opiskelija saa mallivastauksen näkyviin.

### Viestit

- Sekä opettajat että opiskelijat voivat lähettää viestejä keskustelualueella.
- Lähetetyssä viestissä näkyy viestin lähettäjä, kellonaika ja viestin sisältö.
  
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


## Lopullinen palautus
Verrattuna alkuperäiseen suunnitelmaan sovelluksesta on jäänyt joitain toimintoja pois. Kohta "keskeiset toiminnot" kuvaa nyt sovelluksen lopullista tilannetta.

