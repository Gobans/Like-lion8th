/* 
첫 번째로 api에서 받은 key, default 날짜로 구성된 url을 임의로 설정하고 
해당 일자의 rank 데이터를 받아 html에 전송해주는 기초적인 과정을 다뤄볼게요
< Contents >
1. key 받아와 날짜정보를 임의로 작성해서 url로 보내주기
2. async & await & promise object 맛보기
3. rank 데이터 받아서 html에 쏴주기 
*/
let lastDay = new Date((new Date()) - 1000*60*60*24).toISOString().substring(0,10);
let dateInput = document.querySelector(".todayDateInput");
dateInput.value = lastDay;
dateInput.setAttribute("max", lastDay);
let contentsBox = document.querySelector('.contents'); // 그냥 html에 있는 class contents div

let movieCodeObject = {}
let movieNameArray = []
let movieCodeArray = []

const key = "?key=68d721bfd4c8a4cfffc956d0386282ea"; // api key를 가져왔습니다.

 // 검색할 json파일 url 입니다
/* async function은 promise object를 return 합니다 
search 함수를 불러오면 return promise object가 완료될때 까지 기다려줄거에요*/
const clickedSearchBtn = async() => {
    await giveRankObject()
    .then((data) => {
        let DtYear = data.boxOfficeResult.showRange.substring(0,4);
        let DtMonth = data.boxOfficeResult.showRange.substring(4,6);
        let DtDate = data.boxOfficeResult.showRange.substring(6,8);
        // 20200906~20200906 형태에서 원하는 부분만 잘랐어요 
        // 더 간략하게 할 수 있을거 같은데 일단 이렇게!
        let dateTitle = document.createTextNode(`${DtYear}년 ${DtMonth}월 ${DtDate}일 박스 오피스`);
        //appenchild해주기 위해 textnode로 담아 주시고
        let titleBox = document.createElement('h1');
        // h1 태그도 하나 만들어주시고
        let createDiv = document.createElement('div');
        //div도 만들어주시고
        createDiv.classList.add("moviePackage");
        // 만든 div 클래스에 moviePackage 를 추가해 주시고
        contentsBox.appendChild(createDiv).appendChild(titleBox).appendChild(dateTitle);
        // contentsBox 속에 만든 div 그 속에 titleBox(h1 태그) h1태그 글자를 dateTitle로 해줍시다.
        for (let i = 0; i < 10; i++) {
            let movieRankJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieNm; 
            let movieCodeJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieCd; 

            let text = document.createTextNode(`${i+1}위 `+movieRankJson);
            //~~위 를 표시하기 위해 `${i+1}위 `를 추가했어요
            let textBox = document.createElement('button');
            // p태그 만들어주시고
            contentsBox.appendChild(createDiv).appendChild(textBox).appendChild(text);
            // contentsBox 속에 만든 div 그 속에 textBox(p 태그) p태그 글자를 text(~위 영화제목)로 해줍시다.
            textBox.setAttribute("value",`${movieRankJson}`)
            textBox.setAttribute("onclick", "ClickedMovieBtn(this)")

            movieNameArray[i] = `${movieRankJson}`
            movieCodeArray[i] = `${movieCodeJson}`
            movieCodeObject[movieNameArray[i]] =`${movieCodeArray[i]}`
            
        };
        console.log(movieCodeObject)
    })
    .catch(error => console.log(`에러 발생 ${error.name}:${error.message}`));
};
const giveRankObject = async() => {
    let date = document.todayDateForm.todayDateInput.value
    let targetDate = date.replaceAll("-","")

    let targetTodayDate = `&targetDt=${targetDate}`; // 검색형식이에요
    const url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    + key
    + targetTodayDate
    const response = await fetch(url);

    return await response.json(); // text, arrayBuffer, blob, json, formData 종류가 있어요
}

const showMeTheCode = async(clickedValue)=>{
    let iWantedValue = clickedValue.value
    console.log(iWantedValue)
    let code = await CodeInMovieObj(iWantedValue)
    let Info = searchMoreInfo(code)
    console.log(Info)
}

const CodeInMovieObj = async(ClickedValue) => {
    let iWantedCode = movieCodeObject[ClickedValue]
    return await iWantedCode
}

const searchMoreInfo = async(code) =>{
    let usingCode = `&movieCd=${code}`
    console.log(usingCode)
    const infoUrl = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
    + key
    + usingCode;
    const responseInfo = await fetch(infoUrl)
    console.log(infoUrl)
    return await responseInfo.json()

}

const ClickedMovieBtn = async(clickedValue)=>{
    await showMeTheCode(clickedValue)
        .then((info)=>{
            console.log(info)
            console.log("이제가공남음")
        })
}


/* 기다림이 끝나고 promise object를 data라는 (임의)이름으로 사용할거에요
.then()을 통해서 promise object 가공합니다.*/


/* fetch(url, {
    method="GET",
    headers={
        'Content-Type': 'application/json',
        '필요하다면' : '이렇게 보내요'
      }
})
    .then(response => response.json()) 
    .then((data) => {
        for (let i = 0; i < 10; i++) {
            movieRankJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieNm; 
            let text = document.createTextNode(movieRankJson);
            contentsBox.appendChild(text);
        }
    })
    .catch(error => console.log(`에러 발생 ${error.name}:${error.message}`));
 */