
google.charts.load('current', { 'packages': ['corechart'] });


// doughnut chart
google.charts.setOnLoadCallback(drawDoughnutChart);
    function drawDoughnutChart() {
        console.log("in function chart.js")
        var data = google.visualization.arrayToDataTable([
            ['Task', 'Hours per Day'],
            ['Work', 11],
            ['Eat', 2],
            ['Commute', 2],
            ['Watch TV', 2],
            ['Sleep', 7]
        ]);

        var options = {
            title: 'My Daily Activities',
            pieHole: 0.4,
        };

        var chart = new google.visualization.PieChart(document.getElementById('doghnutChart'));
        chart.draw(data, options);
    }




// pie chart
google.charts.setOnLoadCallback(drawPieChart);
function drawPieChart() {

    var data = google.visualization.arrayToDataTable([
        ['Task', 'Hours per Day'],
        ['Work', 11],
        ['Eat', 2],
        ['Commute', 2],
        ['Watch TV', 2],
        ['Sleep', 7]
    ]);

    var options = {
        title: 'My Daily Activities'
    };

    var chart = new google.visualization.PieChart(document.getElementById('myChart'));

    chart.draw(data, options);
}