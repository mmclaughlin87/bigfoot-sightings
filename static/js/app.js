/* data route */
var url = "/data";


function buildPlot() {
    // YOUR CODE HERE
    // fetch the data from your api
    // plot the results

    Plotly.d3.json(url, function(error,response){
        if (error) return console.warn(error);
        var layout = {
            title:"Bigfoot Sightings By Year"
        };
        var data = response;
        Plotly.newPlot('plot', data, layout)
    })
}

buildPlot();
