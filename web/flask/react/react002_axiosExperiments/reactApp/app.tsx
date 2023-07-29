import * as React from 'react'
import { createRoot } from 'react-dom/client';
import { useState } from 'react';

/*
Working on following this guide: https://reactjsexample.com/hello-react-create-a-minimalist-react-app/

And this react docs: https://react.dev/learn/state-a-components-memory
*/


function App() {
    const [index, setIndex] = useState(0);

    function onClick(){
        setIndex(index + 1);
    }

    return(
        <div>
            <h2>App</h2>
            <div>Click count: {index}</div>
            <button onClick={onClick}>Click Me!</button>
        </div>
    );
}

const domNode = document.getElementById('root');
const root = createRoot(domNode)
  
root.render(<App />);