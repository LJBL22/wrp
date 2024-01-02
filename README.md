# 🧧 Taiwanese Wedding Red Packet Calculator 🧧

#### Video for Demo: Youtube [URL](https://youtu.be/-ShM5qkQY1Y?si=Beq2SDdATjHn6m0G)

#### Description:

### How to demo 
#### - [DEMO SITE](https://wrp-self.vercel.app/) supported by vercel
* NOTICE: this link is only for static demo, if you need to execute the db, you need to download locally due to VERCEL is a serverless service which does not support SQLite.

#### - Before deploy to vercel
1. Download this repo.
2. Create a Flask Python environment in the directory using your IDE. For Visual Studio Code, you can follow [this instructions](https://code.visualstudio.com/docs/python/tutorial-flask).
3. If the process did not execute automatically, you may need to install the required dependencies (see requirements.txt).
4. Make sure to start a new terminal.
5. Type `flask run` in the terminal within the project directory.

### Tools and packages used in development

- python
- flask
- sqlite
- bootstrap

### Features

- To assist users in calculating the appropriate amount for a red packet, taking into account various factors.
- Review the checking records.

### Idea Background:

#### Taiwanese Wedding Red Packet Etiquette

A red packet or a red envelope is a monetary gift given during holidays or for special occasions such as a wedding. ---[Wikipedia](https://en.wikipedia.org/wiki/Red_envelope)

In Taiwan, for guests attending weddings, the customary red envelope gift typically starts at NTD 600. When estimating a total gift amount of less than 10,000 NTD, it is advisable to steer clear of the numbers 4 and 8. This caution stems from cultural nuances, where the number 4 is associated with the word for "death," and the number 8, while considered “wealth” in many contexts, sounds similar to the word for "separation." Thus, it may not be deemed suitable for inclusion in wedding gift amounts. Additionally, one should avoid having an odd digit, which related to funerals, or the digit 0 in the hundreds place, following established conventions.

Interestingly, the amount of NTD 9,900 is considered especially auspicious. This is due to its homophonic sound "jiu-jiu" in Mandarin, symbolising a heartfelt wish for enduring marital happiness.

In the event that the gift amount exceeds 10,000 NTD, it is recommended to minimise the presence of two or more odd digits and to avoid the numbers 4 and 8 whenever possible.

However, regardless of the size of the gift you present, the most crucial aspect lies in the sincerity of your well-wishes for the newlyweds. May your contribution be a token of blessings that accompany them on their journey into marital bliss.

### structure

```bash
.
├── Pipfile
├── README.md
├── app.py
├── price.db
├── requirements.txt
├── static
│   └── style.css
├── templates
│   ├── calculator.html
│   ├── error.html
│   ├── index.html
│   ├── layout.html
│   └── records.html
└── vercel.json
```

### pages functions

#### style

- majorly bootstrap
- plain css

#### templates

- index.html: introduce the custom and the basic principles that follow to calculate the cash of red packet
- calculator.html: first I wrote the main function, and refactor the style at last.
- error.html: debug for users who forget to choose an option
- layout.html: layout, most important structure of flask/jinja
- records.html: history of calculating records

#### files

- app.py: main function, the logic of calculator took me a lot of time to calculate to a reasonable fomula.
- price.db: db of sqlite
- README.md: me
- requirements.txt: for python & flask
