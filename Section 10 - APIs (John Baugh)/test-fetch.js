
function start() {
    const btnGetData = document.getElementById('btn_get_data');
    btnGetData.onclick = getPageViewsForTopic;
}//end start

function getPageViewsForTopic() {
    let searchTerm = document.getElementById('search_term').value;
    let outputSpan = document.getElementById('output');

    let viewTotal = 0;

    outputSpan.innerHTML = "<h2>Results for " + searchTerm + "</h2>";  

    searchTerm = searchTerm.charAt(0).toUpperCase() + searchTerm.slice(1);

    console.log(searchTerm);

    
    fetch(`https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/${searchTerm}/daily/20220901/20221001`)
        .then((response) => response.json())
        .then((data) => {
            const dataArray = data.items;
            dataArray.forEach((dayData) => {
                const dateData = dayData.timestamp;
                const year = dateData.slice(0, 4);  //e.g., 2022
                const month = dateData.slice(4, 6);  //e.g., 09
                const day = dateData.slice(6, 8);    //e.g., 01
                const dateString = `${year}-${month}-${day}`;

                //display the data
                outputSpan.innerHTML += dateString + ":&nbsp;&nbsp;";
                outputSpan.innerHTML += dayData.views + "<br>";

                viewTotal += parseInt(dayData.views);
            });//end for each

            outputSpan.innerHTML += "<br><br><strong>Total: &nbsp;&nbsp;" + viewTotal;
        });

}//end getPageViewsForTopic

window.onload = start;