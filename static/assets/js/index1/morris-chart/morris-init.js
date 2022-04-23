

// bar chart

Morris.Bar({
    element: 'bar-chart',
    data: [
        {x: '2015 Q1', y: 2, z: 4, a: 3},
        {x: '2015 Q2', y: 2, z: null, a: 1},
        {x: '2015 Q3', y: 0, z: 2, a: 4},
        {x: '2015 Q4', y: 2, z: 4, a: 3}
    ],
    xkey: 'x',
    ykeys: ['y', 'z', 'a'],
    labels: ['Y', 'Z', 'A'],
    gridLineColor: '#e5ebf8',
    barColors:['#36a2f5','#A768F3','#eac459']

});


var day_data = [
    {"elapsed": "I", "value": 8},
    {"elapsed": "II", "value": 34},
    {"elapsed": "III", "value": 53},
    {"elapsed": "IV", "value": 12},
    {"elapsed": "V", "value": 13},
    {"elapsed": "VI", "value": 22},
    {"elapsed": "VII", "value": 5},
    {"elapsed": "VIII", "value": 26},
    {"elapsed": "IX", "value": 12},
    {"elapsed": "X", "value": 19}
];

// line chart

Morris.Line({
    element: 'line-chart',
    data: day_data,
    xkey: 'elapsed',
    ykeys: ['value'],
    labels: ['value'],
    gridLineColor: '#e5ebf8',
    lineColors:['#FF518A'],
    parseTime: false,
    lineWidth: 1
});

