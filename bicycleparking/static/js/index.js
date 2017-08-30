import Navigo from 'navigo';
import questions from './survey-questions';
import Question from './question';
import '../css/app.css';

class Survey {
  constructor() {
    this.steps = {};
    this.router = new Navigo('/', true);
    this.steps = questions.map((question, i) => {
      let props = question;
      if (i + 1 === questions.length) {
         props = Object.assign({}, props, {
           final: true
         })
      }
      return new Question(props, this)
    })
    try {
      this.state = localStorage.getItem('survey_state') ? JSON.parse(localStorage.getItem('survey_state')) : {};
    } catch (err) {
      this.state = {};
    }
    this.router.on({
      'survey/:step': (params, query) => {
        this.renderStep(params, query)
      },
    }).resolve();
  }

  navigate() {
    const next = parseInt(this.router.lastRouteResolved().params.step, 10) + 1;
    this.router.navigate(`/survey/${next}`)
  }

  submit() {
    console.log(this.state)
  }

  setState(newState) {
    this.state = Object.assign({}, this.state, newState);
    localStorage.setItem('survey_state', JSON.stringify(this.state));
  }

  renderStep(params, query) {
    let step = params.step;
    this.steps[step].render();
  }
}

new Survey();
