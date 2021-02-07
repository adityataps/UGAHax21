import React, { Component } from 'react'

import CanvasJSReact from "../../assets/canvasJS/canvasjs.react";

var CanvasJS = CanvasJSReact.CanvasJS
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class SalesLine extends Component {

    render() {
        const options = {
            title: {
                text: "Basic Column Chart in React"
            },
            data: [{
                type: "spline",
                dataPoints: [
                    { label: "Apple",  y: 10  },
                    { label: "Orange", y: 15  },
                    { label: "Banana", y: 25  },
                    { label: "Mango",  y: 30  },
                    { label: "Grape",  y: 28  }
                ]
            }]
        }

        return (
            <div>
                <CanvasJSChart options = {options}
                    /* onRef = {ref => this.chart = ref} */
                />
            </div>
        );
    }
}

export default SalesLine