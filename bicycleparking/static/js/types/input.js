export default class Input {
  constructor(props, question) {
    this.props = props;
    this.submit = question.submit;
    this.onError = question.onError;
    this.onMessage = question.onMessage;
    this.router = question.router;
  }
  
  get value() {
    return document.getElementById('input').value;
  }

  bind() {}
}