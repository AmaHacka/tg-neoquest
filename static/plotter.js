function buildLabels(dump) {
    console.log(dump);
    let chartData = [];
    chartData.push(new Date(Date.parse(dump[0].time)));
    for (let i = 1; i < dump.length; i++) {
        chartData.push(new Date(new Date(Date.parse(dump[i].time)).getTime() - 1000));
        chartData.push(new Date(Date.parse(dump[i].time)))
    }
    return chartData
}

function buildValues(dump) {
    let chartData = [];
    let lastStatus = dump[0].status ? 0.1 : 0;
    chartData.push(lastStatus);
    for (let i = 1; i < dump.length; i++) {
        chartData.push(lastStatus);
        chartData.push(dump[i].status ? 0.1 : 0);
        lastStatus = dump[i].status ? 0.1 : 0;
    }
    return chartData
}

let ctx = document.getElementById("onlineChart");


$(".user").on('click', function () {
    $.get("/api/" + $(this).attr("data-id"), function (data) {
        data = JSON.parse(data);
        let myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: buildLabels(data),
                datasets: [{
                    label: "Активность пользователя",
                    data: buildValues(data),
                    // borderColor: "#3e95cd",
                    pointRadius: 1,
                    pointHoverRadius: 1
                }]
            },
            options: {
                scales: {

                    yAxes: [{
                        ticks: {
                            suggestedMin: 0,
                            suggestedMax: 1,
                            stepSize: 1,
                        }
                    }],
                    xAxes: [{
                        type: 'time',
                        time: {
                            unit: 'minute',
                        },
                        distribution: 'linear',
                    }],
                },
                elements: {
                    line: {
                        tension: 0
                    }
                }
            }
        });
    });
    console.log($(this).attr("data-id"));
});


