import Input from './input';

export default class DateTimeInput extends Input {

  constructor() {
    super(...arguments);    
    this.values="";
  }

  get value() {
    return this.values;
  }

  bind() {
    $('.datepicker').pickadate({
      selectMonths: true, 
      selectYears: 15,
      today: 'Today',
      clear: 'Clear',
      close: 'Ok',
      closeOnSelect: false 
    });
  }

  get template() {
    return (`
        <input  id="input" type="text" class="datepicker" name=${this.props.key}>
      `
    )
  }
}