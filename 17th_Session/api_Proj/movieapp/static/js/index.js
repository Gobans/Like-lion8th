const key = "?key=68d721bfd4c8a4cfffc956d0386282ea"
let itemPerPage= `&itemPerPage=20`
var title = document.getElementById('a')

const url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'
             + key
             + itemPerPage

fetch(url)
.then(response=>response.json())
.then(function(msg){
    for(var i =0; i<20; i++){
        var div = document.createElement('div');
        var low_div = document.createElement('div')
        var title_div = document.createElement('div')
        var br = document.createElement('br');

        var mp = document.createElement('p');
        mp.id = 'movieNm'
        var np = document.createElement('p');
        np.id = 'nationAlt'
        var gp = document.createElement('p');
        gp.id = 'genreAlt'
        var pp = document.createElement('p');
        pp.id = 'prdtYear'
        title_div.id = 'title_div'
        low_div.id = 'low_div'
        div.id = 'movies'
        short_url = msg.movieListResult.movieList[i]
        console.log(short_url);
        div.appendChild(title_div)
        div.appendChild(low_div)
        title.appendChild(div);
        var movieNm = document.createTextNode(short_url.movieNm);
        var nationAlt = document.createTextNode(short_url.nationAlt);
        var genreAlt = document.createTextNode(short_url.genreAlt);
        var prdtYear = document.createTextNode(short_url.prdtYear);
        
        mp.appendChild(movieNm);
        np.appendChild(nationAlt);
        gp.appendChild(genreAlt);
        pp.appendChild(prdtYear);

        title_div.appendChild(mp);
        low_div.appendChild(br);
        low_div.appendChild(np);
        low_div.appendChild(gp);
        low_div.appendChild(pp);




    }
            
});