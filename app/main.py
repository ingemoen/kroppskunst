import uuid
import os
import pprint
from flask import Flask, request, session, render_template, Response

app = Flask(__name__)
app.debug = True

redis_host = os.getenv('REDIS_SERVER', 'redis')
app.config['SECRET_KEY'] = os.getenv('REDIS_SERVER', 'ChangeThis')

# from lib.lib import getOrder, setOrder


@app.route('/')
def index():
    setup = { 
        'id' : '10000',
        'siteName' : 'SætreHonning',
        'host' : request.environ['HTTP_HOST']
    }
    stories = [
        {'header' : 'Sætrehonning', 'align' : 'right',  'img' : 'kuber.jpg', 'text' : '<p>Jeg har så lenge jeg kan huske vært fasinert av bier.  Som liten lå jeg ofte bak noen busker og smugtittet på biene til en birøkter litt lengre oppe i gata. Jeg husker jeg kunne ligge der i timesvis og se på biene fly inn og ut av kubene.</p><p>Som godt voksen ble drømmen om å bli røkter selv til virkelighet. Jeg meldte meg på et kurs hos ByBi i Oslo og kjøpte mine første to kuber våren 2019.</p><p>Det var ikke aktuelt for kona med noen bigård i hagen, så jeg startet opp i hagen til svigermor. Når første sommer var over, var 2 kuber blitt til 4 kuber og det var produsert 36kg honning.</p><p>Sesongen 2020 utvidet jeg med en bigård i eplehagen på Werpen, og en bigård på Mørk Gård. 4 kuber ble i sesongen 2020 til 18 kuber fordelt på 3 bigårder.</p><p>Fra sesongen 2021 er planen å øke til en stabil drift på mellom 25 og 35 bikuber, fordelt på 3 bigårder. I tillegg skal jeg i et sammarbeid med Håøya Naturverksted produsere HåøyaHonning ute på Håøya.</p>'},
        {'header' : 'Kjøpe Sætrehonning', 'align' : 'left', 'img' : 'butikk.jpg', 'text' : '<bl><li>Ta deg en tur innom Sætre Frukt og Grønt i Sætre sentrum. Der finner du Sætrehonning som du kan ta med deg hjem i dag. Sætre Frukt og Grønt har også søndagsåpent.</li><li>Direkte fra meg. Send en melding til Sætrehonning på Facebook, så leverer jeg Sætrehonning på døra i Sætre og Åros.</li><li>REKO Ringen - Asker. Av og til stiller jeg på REKO Ringens utlevering i Asker</li></bl><br/><br/><b>Jeg har fremdeles Sensommerhonning igjen for salg, Sommerhonningen er desverre utsolgt og kommer inn på lager igjen midtsommer 2021.</b></p>'},
        {'header' : 'Sommersesongen', 'align' : 'right', 'img' : 'bier.mov#t=0.5', 'text' : '<p>Hele sommersesongen er biene opptatt med å besøke blomster i nærmiljøet her på Sætre.</p><p>Biene flyr opptil 3 km fra kubene og dekker dermed et område på fantastiske 28 kvadratkilometer. Lurer på hvor mye det er ? Tenk deg et område som er tusen meter bredt og som strekker seg fra Sætre Sentrum til Slottet i Oslo. Ganske imponerende.</p><p>Biene fra SætreHonning trekker på blomster i et område avgrenset av Åros, Håøya, Steinerskolen og Sandspollen. Bor du i dette området har du nesten garantert hatt besøk fra en bie fra Sætrehonning.</p>'},
        {'header' : 'Honningen',  'align' : 'left','img' : 'sommerhonning.jpg', 'text' : ' <p>Honningen biene produserer er fra blomster i Sætre og nærmiljøet rundt. Kjøper du SætreHonning så støtter du aktivt pollineringen og faunaen her på Sætre.</p><p><b>Sommerhonning</b><br/>Sommerhonning er honning som biene har produsert før lyngen blomstrer en eller annen gang i juli.  Den består av blomster fra alle hagene her i Sætre, blåbær, tyttebær, lind og bringebær.Ettersom det er bringebær, og spesielt villbringebær som gir mest nektar, er denne dominerende i Sommerhonningen. Sommerhonningen er søt og mild på smak.<br/><br/><b>Sensommerhonning med Lyng</b><br/>Sensommerhonning er honning som biene høstes etter at lyngen blomstret. Ettersom jeg ikke flytter kubene opp på lyngmarkene i fjellet, men lar biene utnytte lyngen her i skogen på Sætre, vil ikke honningen være en ren Lynghonning. Sensommerhonningen vil inneholde lyng, kløver og andre blomster som viser sin prakt litt sent på sommeren. Sensommerhonningen vil også inneholde litt sommerhonning som jeg har valgt å ikke høste tidligere.Sensommerhonningen er mere markant i smaken, mørkere, men ikke så kraftig som ren Lynghonning.<br/><br/><b>Sommerhonning med smak</b><br/>Jeg kommer fra sesongen 2021 også til å produsere Sommerhonning med Chilli, Sommerhonning med Ingefær og Sommerhonning med Kanel. Dette gleder jeg meg realt til og det skal bli morro med tilbakemeldinger.</p>'}
    ]
    return render_template('index.html', setup=setup, stories=stories)

@app.route("/test")
def test():
    str = pprint.pformat(request.environ, depth=5)
    return Response(str, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)