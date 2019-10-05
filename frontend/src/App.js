import React, {Component} from 'react';
import ScriptBuilder from './components/ScriptBuilder';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import './App.css'

class App extends Component {
    state = {
    };

    componentDidMount() {
    }
    render() {
        return (
            <div>
                <Router>
                    <div>
                        <Switch>
                            <Route path='/script-builder' component={ScriptBuilder}/>
                        </Switch>
                        {/*<Footer />*/}
                    </div>
                </Router>
            </div>
        );
    }
}

export default App;
