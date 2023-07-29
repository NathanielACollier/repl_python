import * as React from 'react'
import { createRoot } from 'react-dom/client';

/*
Working on following this guide: https://reactjsexample.com/hello-react-create-a-minimalist-react-app/
*/

class App extends React.Component {
    state = { myCounter: 3 }
    
    onClick(){
        this.setState({
            myCounter: this.state.myCounter + 1
        });
    }

    render(){
      return(
        <div>
            <h2>App</h2>
            <div>Click count: {this.state.myCounter}</div>
            <button onClick={this.onClick}>Click Me!</button>
        </div>
      );
    }
}

const domNode = document.getElementById('root');
const root = createRoot(domNode)
  
root.render(<App />);