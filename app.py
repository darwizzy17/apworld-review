import os
import random
import json

import streamlit as st

# ---------- OPTIONAL: OpenAI client for AI-generated questions ----------
OPENAI_ENABLED = False
client = None
try:
    from openai import OpenAI

    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        OPENAI_ENABLED = True
except Exception:
    OPENAI_ENABLED = False
    client = None

# ---------- STUDY GUIDE CONTENT (Markdown) ----------

STUDY_GUIDE_MD = r"""
# Unit 5: Revolutions & Industrialization (c. 1750–1900)

## Big Picture
- Enlightenment + Scientific Revolution → new ideas about **reason, natural rights, social contract, progress**.
- These ideas helped spark the **Atlantic Revolutions** and later **nationalist** and **feminist** movements.
- The **Industrial Revolution** transformed economies, societies, and the environment, and triggered new **political ideologies** (liberalism, socialism, communism, anarchism).
- Artistic movements (Rococo, Neoclassicism, Romanticism, Realism) reflected and reacted to these changes.

---

## 1. Scientific Revolution ➜ Roots of the Enlightenment

**Main shifts**
- From **Church/traditional authority** → **observation, experimentation, reason**.
- Developed **scientific method**: hypothesis, testing, evidence.
- Transformed astronomy, physics, biology, optics and encouraged **skepticism** of accepted truths.

**Key figures**
- **Copernicus** – heliocentric model (Sun at center); challenged geocentrism.
- **Kepler** – three laws of planetary motion; elliptical orbits.
- **Galileo** – improved telescope; observed Jupiter’s moons, phases of Venus, mountains on the Moon; work on motion; tried for heresy.
- **Bacon** – inductive reasoning, “knowledge is power,” modern scientific method.
- **Descartes** – rationalism (“I think, therefore I am”), emphasis on doubt and reason.
- **Newton** – laws of motion and universal gravitation; work in optics; links earlier scientists together.

---

## 2. Enlightenment

**Core ideas**
- **State of nature** & **social contract** – people create gov’t for protection/order.
- **Natural rights** – life, liberty, property.
- **Empiricism** – knowledge from experience (Locke, Bacon).  
- **Rationalism** – knowledge from reason (Descartes).  
- **Deism** – God created universe but doesn’t interfere; rejection of miracles/superstition.
- Emphasized **reason, progress, secularism, individual rights**, reform of gov’t and society.

**Major thinkers**
- **Hobbes** – pessimistic view of humans; need strong absolute ruler for order; wrote *Leviathan*.
- **Locke** – optimistic view; natural rights, right to revolt if gov’t fails; influenced liberalism and democratic revolutions.
- **Montesquieu** – separation of powers; checks & balances.
- **Voltaire** – criticized Church/state corruption; free speech; religious tolerance; deism.
- **Rousseau** – *Social Contract* is with the **general will**; popular sovereignty; men and women are “naturally” different.
- **Beccaria** – reform of criminal justice; opposed torture and excessive punishments, argued punishments should fit crimes.
- **Adam Smith** – capitalism; laissez-faire; division of labor; wealth can be created (not fixed).
- **Diderot** – *Encyclopedia* to compile and spread knowledge.
- **Mary Wollstonecraft** – *Vindication of the Rights of Woman*; argued Enlightenment rights should apply to women.

---

## 3. Atlantic Revolutions

### Common causes
- Enlightenment ideas (popular sovereignty, individual rights, equality before law).
- Social tensions and economic pressures.
- High taxes/imperial control without representation.
- Inspiration from other revolutions.

### American Revolution
- Causes: British taxation (Stamp, Sugar Acts), no representation in Parliament, desire to protect traditional rights.
- Key ideas: **Declaration of Independence**, **Bill of Rights** – apply Enlightenment to politics.
- Outcomes: Independence, creation of a republic, written constitution; slavery persisted (esp. in South); elites largely kept power.

### French Revolution
- Background: debt (7 Years’ War, American Revolution), unequal taxation (only 3rd Estate pays), bread shortages, privilege of nobility/clergy.
- Key events:
  - **Estates-General** and **Tennis Court Oath** (National Assembly).
  - **Storming of the Bastille** (symbol of royal oppression).
  - **Declaration of the Rights of Man and Citizen** – equality before law, popular sovereignty.
  - **Women’s March on Versailles** – economic + political protest.
  - **Dechristianization** and seizure of Church property.
  - **Execution of Louis XVI and Marie Antoinette**.
  - **Reign of Terror** (Robespierre) – mass executions of “enemies of the revolution”.
- Outcomes:
  - End of feudalism and legal privileges.
  - Experiment with republic; then **Napoleon** rises as emperor.
  - Napoleonic Code spreads equality before law, secular law, meritocracy—but also dictatorship and conquest.
  - After defeat, **Congress of Vienna** restores monarchies (Metternich), redraws European borders, tries to contain nationalism.

### Haitian Revolution
- Social structure: grands blancs (big white planters), petits blancs (poor whites), free people of color (**gens de couleur libres**), enslaved Africans.
- Causes: brutal plantation slavery, racial hierarchy, Enlightenment ideas, influence of French/American Revolutions.
- Leaders: **Toussaint Louverture**, later **Jean-Jacques Dessalines**.
- Outcomes:
  - First successful slave revolt, independence of Haiti.
  - Abolition of slavery, redistribution of land to former slaves.
  - Huge economic/political costs: isolation, “independence debt” to France, instability.

### Latin American Revolutions
- Social structure: peninsulares > creoles > mestizos > indigenous & enslaved.  
- Causes:
  - Creole resentment of peninsulares and imperial control.
  - Enlightenment + example of other revolutions.
  - **Napoleonic wars** (Spanish/Portuguese kings displaced → power vacuum).
- Key figures: **Simón Bolívar** (Jamaica Letter), **Miguel Hidalgo**, **José Morelos**, **Tupac Amaru**.
- Outcomes:
  - Independence for many states, but continued inequality.
  - Creole elites kept power; limited social change.
  - Economically dependent on foreign investment and technology.

---

## 4. Effects of Revolutions: Abolition, Nationalism, Feminism

### Abolition of Slavery
- Haiti’s success and slave revolts (e.g. Great Jamaica Revolt) pressured empires.
- **Abolitionist movement** – Quakers, **William Wilberforce**, activists using pamphlets, petitions, boycotts.
- Britain bans slave trade (1807), then slavery (1830s); others follow (Latin America by 1850s, U.S. 1865, Brazil 1888, Russian serfs freed 1861).
- Limits: former slaves often remain poor; sharecropping and indentured labor replace slavery; racism persists.

### Nationalism
- Idea that people sharing language, culture, history, and territory form a **nation**.
- Helped unify:
  - **Italy** (Cavour, Garibaldi) and **Germany** (Bismarck; realpolitik).
  - Greeks & Serbs vs. Ottoman Empire.
- Inspired resistance:
  - Poles, Ukrainians, Czechs, Irish, etc. against empires.
  - **Zionism** – Jewish movement to Palestine.
  - Indian, Arab, and Egyptian national movements.
- Distinction:
  - **Patriotism** – pride in country, allows criticism.
  - **Nationalism** – can be exclusive and intolerant.

### Feminism
- Enlightenment ideas + revolutionary ideals extended to women:
  - **Wollstonecraft**, **Olympe de Gouges**, **Seneca Falls Convention** (Stanton, “all men and women are created equal”).
- 19th–early 20th century:
  - Suffrage movements (New Zealand 1893; U.S. 1920; France 1945).
  - **Maternal feminism** – claim women must participate in politics to protect families.
  - Activists like **Emmeline Pankhurst** use militant tactics in Britain.

---

## 5. Industrial Revolution (First & Second)

### Why Britain?
- Coal & iron, access to water transport, stable gov’t & property laws, capitalist culture, agricultural revolution (enclosure ➜ surplus labor), colonies for markets and raw materials.

### What changed?
- Mechanization of **textiles** first (spinning jenny, power loom), then iron & steel, railroads, steamships.
- **Steam engine**, fossil fuels (coal, later oil).
- Factory system → specialization of labor.

### Impacts
- Economic:
  - Massive increase in production and wealth.
  - Lower cost of goods, consumer society.
- Social:
  - **Urbanization**; growth of new **middle class** and **working class**.
  - Crowded cities, pollution, disease, crime.
  - Gendered division of labor; “separate spheres” for middle-class women.
- Environmental:
  - Extraction of nonrenewable resources, pollution of air and water.

### Reactions & Ideologies
- Workers form **trade unions**; strikes, demands for higher wages and shorter hours.
- **Luddites** – attacked machines that threatened artisan jobs.
- **Utilitarianism** (Bentham, Mill) – greatest good for greatest number; support reforms.
- **Utopian socialists** (Owen, Fourier, Saint-Simon) – model communities, cooperative ownership.
- **Marx & Engels** – “scientific socialism,” class struggle (bourgeoisie vs. proletariat), predicted proletarian revolution and classless society.
- **Anarchists** (e.g. Bakunin) – all gov’t corrupt, want stateless society, sometimes use violence.
- Governments slowly introduce reforms: child labor laws, factory acts, public health reforms, education, expansion of suffrage.

### Second Industrial Revolution
- New energy sources: **electricity** and **oil**.
- New industries: steel, chemicals, telegraph/telephone, internal combustion engine.
- Mass production + assembly line → consumer goods (bikes, canned food, appliances).
- More women in workforce (textiles, clerical, teaching, nursing); fuels suffrage movements.

---

## 6. Capitalism & Economic Developments

- **Mercantilism** – earlier system; wealth viewed as fixed; goal was to hoard bullion and regulate trade.
- **Industrial capitalism** – private ownership of means of production; profit motive; investment & innovation expand wealth.
- Tools: stock markets, limited-liability corporations, international banks (e.g. HSBC), joint-stock companies.
- Globalization:
  - Demand for raw materials ➜ imperialism & extraction in colonies.
  - Migrants move for work (Europe → Americas, Australia, etc.).

---

## 7. Social Classes in Industrial Society

- **Aristocracy** loses economic dominance but retains prestige.
- **Upper middle class** – factory owners, bankers; often join old elites.
- **Middle class** – professionals; value respectability, thrift, hard work.
- **Lower middle class** – clerks, salespeople, office workers; big growth.
- **Working class** – factory/mining labor; long hours, low wages, harsh conditions.

---

## 8. Political Spectrum (19th-century)

- **Radicals** – far left; rapid, sweeping change; sometimes revolutionary.
- **Liberals** – reform within system; constitutionalism; civil rights; free markets.
- **Moderates** – compromise; gradual change.
- **Conservatives** – preserve tradition; wary of rapid change.
- **Reactionaries** – far right; want to return to “old order”; might support authoritarian rule.

---

## 9. Art & Ideas: Rococo, Neoclassicism, Romanticism, Realism

### Rococo
- Early 1700s; light, playful, decorative; aristocratic audiences.
- Pastel colors, romance, leisure. Fragonard, Boucher.

### Neoclassicism
- Inspired by Greece/Rome; serious, moral, symmetrical.
- Linked to Enlightenment and French Revolution virtues.
- Jacques-Louis David (e.g. *Napoleon Crossing the Alps*); classical music (Haydn, Mozart).

### Romanticism
- Reaction against Enlightenment’s cold rationalism and Industrial ugliness.
- Emphasizes **emotion, imagination, nature, the sublime, nationalism, mysticism**.
- Literature: Wordsworth, Keats, Goethe, Byron, Shelley, Hugo.
- Art: Goya (*Third of May 1808*, *Saturn Devouring His Son*), Turner (*The Slave Ship*), Constable.
- Music: Beethoven, Chopin, program music, virtuosos (Liszt, Paganini).
- Themes: individual hero, national identity, awe of nature, critique of industrial society.

### Realism
- Focus on ordinary life, especially working class; gritty and honest.
- Highlights social problems of industrialization.
- Literature: Dickens, Flaubert; Art: Courbet, Millet; photography emerges.

---

## 10. Swift’s *A Modest Proposal* (Contextual Lit)

- Satirical pamphlet “proposes” eating Irish babies to solve poverty.
- Uses extreme irony to criticize British policies and indifference to Irish suffering.
- Fits broader 18th–19th c. trend of literature critiquing inequality and social injustice.

---

Use this guide with your flashcards and MCQs to link **people, ideas, events, and themes** across the whole 1750–1900 unit.
"""

# ---------- FLASHCARDS (TERM ➜ DEFINITION) ----------

FLASHCARDS = [
    # Enlightenment & Scientific Revolution
    {"term": "State of Nature", "definition": "Hypothetical condition before organized government, used to justify forming political systems and social contracts."},
    {"term": "Social Contract", "definition": "Agreement in which people give up some freedoms to governments in exchange for protection and order."},
    {"term": "Deism", "definition": "Belief that God created the universe and natural laws but does not intervene with miracles."},
    {"term": "Empiricism", "definition": "Theory that knowledge comes mainly from sensory experience and observation."},
    {"term": "Rationalism", "definition": "Theory that reason and innate ideas are key sources of knowledge."},
    {"term": "Thomas Hobbes", "definition": "English thinker who argued humans are selfish and need an absolute ruler for order; wrote 'Leviathan'."},
    {"term": "John Locke", "definition": "Philosopher who argued for natural rights of life, liberty, property and right to overthrow tyrannical gov’t."},
    {"term": "Montesquieu", "definition": "Enlightenment thinker who proposed separation of powers and checks and balances."},
    {"term": "Voltaire", "definition": "Critic of Church and absolutism; defended free speech and religious tolerance; deist."},
    {"term": "Rousseau", "definition": "Believed in general will and popular sovereignty; wrote 'The Social Contract'."},
    {"term": "Adam Smith", "definition": "Father of modern economics; promoted laissez-faire capitalism and free markets in 'Wealth of Nations'."},
    {"term": "Mary Wollstonecraft", "definition": "Early feminist who argued for equal education in 'A Vindication of the Rights of Woman'."},

    # Atlantic Revolutions
    {"term": "Popular Sovereignty", "definition": "Political principle that power comes from the people rather than a monarch."},
    {"term": "Third Estate", "definition": "Commoners in pre-revolutionary France who paid most taxes and had the least privilege."},
    {"term": "Declaration of the Rights of Man and Citizen", "definition": "French Revolutionary document asserting equal rights and popular sovereignty."},
    {"term": "Reign of Terror", "definition": "Radical phase of French Revolution when Robespierre’s government executed thousands of 'enemies'."},
    {"term": "Toussaint Louverture", "definition": "Leader of the Haitian Revolution who helped turn a slave revolt into a movement for independence."},
    {"term": "Gens de couleur libres", "definition": "Free people of color in colonial Saint-Domingue (Haiti)."},
    {"term": "Simón Bolívar", "definition": "Creole revolutionary who led independence movements in northern South America; wrote the Jamaica Letter."},
    {"term": "Great Jamaica Revolt", "definition": "1831–32 slave uprising in British West Indies that helped push Britain toward abolition."},

    # Nationalism & Feminism
    {"term": "Nationalism", "definition": "Ideology that people who share culture, language, or history should form a self-governing nation-state."},
    {"term": "Realpolitik", "definition": "Politics based on practical considerations of power rather than ideals; used by Bismarck and Cavour."},
    {"term": "Zionism", "definition": "Jewish nationalist movement to establish a homeland in Palestine."},
    {"term": "Maternal Feminism", "definition": "Idea that women should have public roles because they are responsible for protecting children and family."},

    # Industrial Revolution & Ideologies
    {"term": "Industrial Revolution", "definition": "Shift to machine-based manufacturing, factory system, and fossil fuels starting in Britain."},
    {"term": "Urbanization", "definition": "Growth of cities as people move from countryside to work in factories."},
    {"term": "Luddites", "definition": "Skilled artisans who smashed machines that threatened their jobs."},
    {"term": "Trade Unions", "definition": "Organizations of workers that bargain collectively for better wages and conditions."},
    {"term": "Utopian Socialism", "definition": "Vision of cooperative, self-sufficient communities sharing ownership of production."},
    {"term": "Karl Marx", "definition": "German thinker who argued history is class struggle; predicted proletarian revolution and communism."},
    {"term": "Proletariat", "definition": "Industrial working class that sells its labor for wages."},
    {"term": "Bourgeoisie", "definition": "Capitalist middle class that owns factories and other means of production."},
    {"term": "Anarchism", "definition": "Belief that all government is corrupt and should be abolished in favor of cooperative self-rule."},
    {"term": "Utilitarianism", "definition": "Ethical theory that the best action maximizes happiness for the greatest number."},

    # Capitalism & Second IR
    {"term": "Capitalism", "definition": "Economic system in which private owners control production for profit in competitive markets."},
    {"term": "Mercantilism", "definition": "Economic policy where states seek fixed wealth by controlling trade and accumulating bullion."},
    {"term": "Mass Production", "definition": "Producing large quantities of standardized goods, often on an assembly line."},
    {"term": "Second Industrial Revolution", "definition": "Late 19th-century phase with steel, chemicals, electricity, and oil."},

    # Art & Culture
    {"term": "Rococo", "definition": "Light, decorative, playful art style associated with aristocratic leisure in 18th-century France."},
    {"term": "Neoclassicism", "definition": "Serious, moral art inspired by classical Greece and Rome; linked to Enlightenment values."},
    {"term": "Romanticism", "definition": "Artistic movement emphasizing emotion, nature, nationalism, and the sublime."},
    {"term": "Realism (Art)", "definition": "Movement depicting everyday life and social problems realistically, especially of lower classes."},
    {"term": "Virtuoso", "definition": "Performer with extreme technical skill and expressive power (e.g., Liszt, Paganini)."},
]

# ---------- MCQ QUESTION BANK (DIFFICULT AP-LEVEL) ----------

MCQ_QUESTIONS = [
    {
        "question": "Which comparison best captures how Enlightenment political thought influenced both the American and French Revolutions?",
        "options": [
            "Both revolutions used Enlightenment ideas primarily to expand monarchical power over colonial elites.",
            "Both revolutions drew on concepts of natural rights and popular sovereignty, though the French applied them more radically to social hierarchy.",
            "Enlightenment ideas were central to the American Revolution but largely irrelevant to the French Revolution, which focused on religion.",
            "Enlightenment ideas in both cases focused mainly on economic liberalism and had little impact on political institutions."
        ],
        "correct": "B",
        "explanation": "Both revolutions were grounded in natural rights and popular sovereignty; the French went further by attacking noble privilege and the Church."
    },
    {
        "question": "In what way did the Haitian Revolution most clearly challenge prevailing Enlightenment thinking in the Atlantic world?",
        "options": [
            "By demonstrating that constitutional monarchies were superior to republics.",
            "By proving that absolutist monarchs could peacefully abolish slavery.",
            "By forcing European states to grant voting rights to all women.",
            "By extending ideals of liberty and equality to enslaved people, contradicting racist assumptions among many Enlightenment thinkers."
        ],
        "correct": "D",
        "explanation": "Haiti’s slave revolt applied universal rights to enslaved Africans, challenging racial limits many Europeans placed on Enlightenment ideals."
    },
    {
        "question": "Which development in Britain most directly created the labor supply necessary for the early Industrial Revolution?",
        "options": [
            "The abolition of serfdom and manorial obligations in Eastern Europe.",
            "The enclosure movement and agricultural changes that pushed rural workers off the land.",
            "The introduction of universal male suffrage for factory workers.",
            "The destruction of guilds during the French Revolution."
        ],
        "correct": "B",
        "explanation": "Enclosure and agricultural improvements displaced many small farmers and laborers, who then moved to cities and worked in factories."
    },
    {
        "question": "A historian arguing that nationalism was a 'double-edged sword' in the 19th century would most likely cite which pair of examples?",
        "options": [
            "The Seven Years’ War and the American Civil War.",
            "The development of factories and the growth of labor unions.",
            "The unification of Germany and the intensification of rivalries that helped lead to World War I.",
            "The spread of Enlightenment deism and the expansion of Romantic mysticism."
        ],
        "correct": "C",
        "explanation": "Nationalism unified Germany but also sharpened interstate rivalries and militarism, contributing to tensions before WWI."
    },
    {
        "question": "Which best explains why Latin American independence movements produced relatively little social change compared with the Haitian Revolution?",
        "options": [
            "Latin American revolutions were financed entirely by foreign investors who insisted on maintaining slavery.",
            "Creole elites led most Latin American movements and sought political independence while preserving social and economic hierarchies.",
            "The Catholic Church firmly opposed independence everywhere in Latin America, preventing any reforms.",
            "Indigenous peoples controlled most military campaigns and refused to share power with other social groups."
        ],
        "correct": "B",
        "explanation": "Creoles wanted to replace peninsulares but generally kept existing racial and class hierarchies, unlike Haiti’s slave-led revolution."
    },
    {
        "question": "Which statement best compares liberalism and socialism as responses to industrial capitalism?",
        "options": [
            "Both rejected representative government and supported absolute monarchy.",
            "Liberalism emphasized legal equality and free markets, while socialism emphasized reducing economic inequality through collective or state action.",
            "Liberalism favored communal ownership of property, while socialism defended laissez-faire economics.",
            "Both movements agreed that workers should avoid political participation."
        ],
        "correct": "B",
        "explanation": "Liberals wanted constitutional rights and market economies; socialists prioritized tackling inequality via collective ownership or strong state reforms."
    },
    {
        "question": "Which feature of Romanticism most clearly represented a reaction against Enlightenment and Industrial values?",
        "options": [
            "Its admiration for factories and railroads as symbols of human progress.",
            "Its preference for precise scientific analysis of nature over emotional responses.",
            "Its focus on emotion, the sublime in nature, and individual experience rather than pure rationality and mechanization.",
            "Its strict adherence to classical rules of composition and balance in all art forms."
        ],
        "correct": "C",
        "explanation": "Romanticism emphasized emotion, imagination, and wild nature, pushing back against Enlightenment rationalism and industrial urban life."
    },
    {
        "question": "Which of the following is a correct historical distinction between the First and Second Industrial Revolutions?",
        "options": [
            "The First mainly relied on textiles, coal, and steam, while the Second featured steel, chemicals, electricity, and oil.",
            "The First was entirely peaceful, while the Second was defined by constant European wars.",
            "The First took place only in Asia, while the Second occurred only in Europe.",
            "The First focused on consumer goods, while the Second focused only on weapons."
        ],
        "correct": "A",
        "explanation": "First IR: textiles, coal, steam. Second IR: steel, chemicals, electricity, petroleum, new consumer goods."
    },
    {
        "question": "Why did many 19th-century conservatives view the French Revolution as a cautionary example?",
        "options": [
            "Because it proved absolute monarchy to be the only stable political system.",
            "Because the rapid overhaul of traditional institutions led to violence, instability, and eventually a military dictatorship.",
            "Because it showed that democracies could never fight wars successfully.",
            "Because it eliminated nationalism from European politics."
        ],
        "correct": "B",
        "explanation": "Conservatives like Metternich argued that radical change in France unleashed chaos, terror, and Napoleon’s dictatorship."
    },
    {
        "question": "Which best explains why industrial capitalism led to large-scale migration during the 19th century?",
        "options": [
            "Workers were legally forced by governments to migrate to foreign colonies.",
            "Industrial countries had no interest in importing raw materials from other regions.",
            "New transportation technologies and demand for labor encouraged people to move to cities and to other continents for work.",
            "Religious authorities required all peasants to leave their home villages after the Enlightenment."
        ],
        "correct": "C",
        "explanation": "Railroads, steamships, and global labor demand encouraged both rural-to-urban migration and overseas migration."
    },
]

# ---------- AI QUESTION GENERATION (OPTIONAL) ----------

AI_CONTEXT = STUDY_GUIDE_MD[:7000]  # enough context but keep prompt size reasonable


def generate_ai_mcq(topic: str = "Unit 5: Revolutions and Industrialization"):
    """
    Uses OpenAI (if available) to generate one AP-style MCQ.
    Returns a dict similar to entries in MCQ_QUESTIONS or None on failure.
    """
    if not OPENAI_ENABLED or client is None:
        return None

    system_msg = (
        "You are an expert AP World History: Modern teacher. "
        "Write challenging multiple-choice questions for Unit 5 (c. 1750–1900) "
        "covering Enlightenment, Atlantic Revolutions, Nationalism, Industrial Revolution, ideologies, and art movements."
    )
    user_msg = f"""
Using the following context, write ONE difficult AP World History multiple-choice question
about {topic}. It must:

- Focus on higher-order thinking (comparison, causation, continuity/change, evaluation).
- Have exactly 4 answer options labeled A, B, C, D.
- Clearly indicate the single correct option.
- Include a short explanation of why that option is correct.

Context:
{AI_CONTEXT}

Return ONLY valid JSON in this format:
{{
  "question": "...",
  "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
  "answer": "B",
  "explanation": "..."
}}
"""

    try:
        completion = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.9,
        )
        content = completion.choices[0].message.content.strip()
        data = json.loads(content)
        # Normalize keys to match internal format
        correct = data.get("answer", "").strip().upper()[0]
        return {
            "question": data.get("question", ""),
            "options": data.get("options", []),
            "correct": correct,
            "explanation": data.get("explanation", ""),
        }
    except Exception:
        return None


# ---------- STREAMLIT PAGE SETUP ----------

st.set_page_config(
    page_title="WHAP Unit 5 Study Hub",
    layout="wide"
)

st.title("WHAP Unit 5 Study Hub: Revolutions & Industrialization (c. 1750–1900)")

st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Study Guide", "Flashcards", "Practice MCQs", "Practice Test"],
)

if "flashcard_index" not in st.session_state:
    st.session_state.flashcard_index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False
if "current_mcq" not in st.session_state:
    st.session_state.current_mcq = None
if "test_questions" not in st.session_state:
    st.session_state.test_questions = []
if "test_index" not in st.session_state:
    st.session_state.test_index = 0
if "test_score" not in st.session_state:
    st.session_state.test_score = 0
if "test_answers" not in st.session_state:
    st.session_state.test_answers = {}


# ---------- HELPER FUNCTIONS ----------

def get_random_bank_question():
    return random.choice(MCQ_QUESTIONS)


def get_new_mcq(use_ai: bool):
    if use_ai:
        ai_q = generate_ai_mcq()
        if ai_q is not None:
            return ai_q
    # fallback to bank
    return get_random_bank_question()


def display_mcq(q, key_prefix: str):
    st.subheader("Question")
    st.write(q["question"])

    # Radio to pick answer
    choice = st.radio(
        "Select your answer:",
        q["options"],
        key=f"{key_prefix}_choice",
    )

    if st.button("Check answer", key=f"{key_prefix}_check"):
        chosen_index = q["options"].index(choice)
        chosen_letter = "ABCD"[chosen_index]
        correct_letter = q["correct"]
        if chosen_letter == correct_letter:
            st.success(f"Correct! ({correct_letter})")
        else:
            st.error(f"Incorrect. You chose {chosen_letter}, correct is {correct_letter}.")
        if q.get("explanation"):
            st.info(f"Explanation: {q['explanation']}")


# ---------- PAGES ----------

if page == "Study Guide":
    st.header("Full Unit 5 Study Guide")
    st.markdown(
        "Use this as your main reference. Scroll, search (Ctrl+F), and connect it to flashcards and questions."
    )
    st.markdown(STUDY_GUIDE_MD)

elif page == "Flashcards":
    st.header("Flashcards: Key Terms & People")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        card = FLASHCARDS[st.session_state.flashcard_index]
        st.markdown(f"### Term")
        st.markdown(f"**{card['term']}**")

        if st.session_state.show_answer:
            st.markdown("---")
            st.markdown("### Definition")
            st.write(card["definition"])
        else:
            st.info("Click **Show Answer** to reveal the definition.")

        show = st.button(
            "Show Answer" if not st.session_state.show_answer else "Hide Answer"
        )
        if show:
            st.session_state.show_answer = not st.session_state.show_answer
            st.rerun()

    with col1:
        if st.button("◀ Previous"):
            st.session_state.flashcard_index = (st.session_state.flashcard_index - 1) % len(
                FLASHCARDS
            )
            st.session_state.show_answer = False
            st.rerun()

    with col3:
        if st.button("Next ▶"):
            st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % len(
                FLASHCARDS
            )
            st.session_state.show_answer = False
            st.rerun()

    st.caption(
        f"Card {st.session_state.flashcard_index + 1} of {len(FLASHCARDS)}"
    )

elif page == "Practice MCQs":
    st.header("Practice Multiple-Choice Questions")

    st.write(
        "These questions are designed to be **difficult AP-level** and require understanding of context, cause/effect, and comparison."
    )

    if OPENAI_ENABLED:
        mode = st.radio(
            "Question source",
            ["AI-generated (if working)", "From built-in question bank"],
        )
        use_ai = (mode == "AI-generated (if working)")
        if use_ai:
            st.success("AI generation is enabled (requires valid OPENAI_API_KEY).")
    else:
        st.warning(
            "OpenAI not configured. Using built-in question bank only. "
            "To enable AI questions, add OPENAI_API_KEY in Replit Secrets and install the 'openai' package."
        )
        use_ai = False

    if st.button("New Question", key="new_mcq_btn"):
        st.session_state.current_mcq = get_new_mcq(use_ai)
        # Reset any old selection
        st.session_state.pop("mcq_choice", None)
        st.rerun()

    if st.session_state.current_mcq is None:
        st.info("Click **New Question** to begin.")
    else:
        display_mcq(st.session_state.current_mcq, key_prefix="mcq")

elif page == "Practice Test":
    st.header("Full Practice Test")

    st.write(
        "This mode gives you a mini test: a set of questions from the bank (no AI) so you can simulate timed practice."
    )

    num_questions = st.selectbox(
        "Number of questions for this test:",
        [5, 10, 15],
        index=1,
    )

    if st.button("Start / Reset Test"):
        # sample questions from bank
        st.session_state.test_questions = random.sample(
            MCQ_QUESTIONS, k=min(num_questions, len(MCQ_QUESTIONS))
        )
        st.session_state.test_index = 0
        st.session_state.test_score = 0
        st.session_state.test_answers = {}
        st.rerun()

    if not st.session_state.test_questions:
        st.info("Click **Start / Reset Test** to begin a practice test.")
    else:
        q_idx = st.session_state.test_index
        questions = st.session_state.test_questions

        if q_idx < len(questions):
            q = questions[q_idx]
            st.subheader(f"Question {q_idx + 1} of {len(questions)}")
            st.write(q["question"])

            choice_key = f"test_choice_{q_idx}"
            choice = st.radio(
                "Select your answer:",
                q["options"],
                key=choice_key,
            )

            if st.button("Submit Answer", key=f"submit_{q_idx}"):
                chosen_index = q["options"].index(choice)
                chosen_letter = "ABCD"[chosen_index]
                correct_letter = q["correct"]

                st.session_state.test_answers[q_idx] = chosen_letter
                if chosen_letter == correct_letter:
                    st.session_state.test_score += 1
                    st.success(f"Correct! ({correct_letter})")
                else:
                    st.error(f"Incorrect. You chose {chosen_letter}, correct is {correct_letter}.")
                if q.get("explanation"):
                    st.info(f"Explanation: {q['explanation']}")

                st.session_state.test_index += 1
                st.rerun()
        else:
            # Test finished
            total = len(st.session_state.test_questions)
            score = st.session_state.test_score
            st.success(f"Test complete! You scored {score} out of {total}.")
            percent = round(100 * score / total)
            st.write(f"Percentage: **{percent}%**")

            st.write("Review:")
            for i, q in enumerate(st.session_state.test_questions):
                user_ans = st.session_state.test_answers.get(i, "—")
                correct_letter = q["correct"]
                label = "✅" if user_ans == correct_letter else "❌"
                st.markdown(f"**Q{i + 1} {label}** — Your answer: {user_ans}, Correct: {correct_letter}")
                if q.get("explanation"):
                    st.caption(q["explanation"])

            st.info("You can click **Start / Reset Test** above to generate a new set of questions.")
