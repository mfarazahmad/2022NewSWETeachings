import React, {Component} from 'react';

// Sample class component | Has 3 parts: Constructor, HandleFunctions, Render
class SampleForm extends Component {

    // initialize the data
    constructor(props) {

        super(props);

        this.state = {
            pokeData: ['bulbasaur', 'pikachi', 'bitchasaurus']
        };
    }

    // returns jsx
    render() {
        return (
            <div>
                Hey TTHERE!
            </div>
        );
    }

};

export default SampleForm;