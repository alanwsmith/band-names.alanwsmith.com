const templates = {
  content: `
<div data-receive="bandName" class="xlarge-block-padding xxlarge-font-size"></div>
  <div class="xlarge-block-padding">
  <button data-send="bandName">Get a Band Name</button>
</div>`,
};

function setProp(key, value) {
  document.documentElement.style.setProperty(key, value);
}

function shuffleArray(array) {
  let currentIndex = array.length;
  let randomIndex;
  while (currentIndex != 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex],
      array[currentIndex],
    ];
  }
}

export default class {
  #currentName = 0;
  #names = [];

  bittyReady() {
    setProp("--load-hider", "1");
  }

  bandName(_, el) {
    el.innerHTML = this.#names[this.#currentName];
    this.#currentName += 1;
    if (this.#currentName === this.#names.length) {
      this.#currentName = 0;
      shuffleArray(this.#names);
    }
  }

  setup(_, el) {
    this.#names = [...el.querySelectorAll("p")].map((n) => {
      return n.innerHTML;
    });
    shuffleArray(this.#names);
    el.replaceChildren(this.api.makeHTML(templates.content));
    this.api.trigger("bandName");
  }
}
