import React, {Component} from 'react';


class Home extends Component {

    constructor(props) {
        super(props);

        this.state = {
            name: ''
        }

        this.handleClick = this.handleClick.bind(this);
    }

    handleInput = (event) => {
        this.setState({name: event.target.value});
    }

    handleClick = () => {
        alert(this.state.name);

    }

    render() {
        return (
        <div>
            <h2>Hey there {this.state.name} with {this.props.job}</h2>

            <p>Enter in your name:</p>
            <input type='text' onChange={this.handleInput} value={this.state.name} />

            <button onClick={this.handleClick} id="button">Click Me</button>
        </div>
        );
    }

}


export default Home;