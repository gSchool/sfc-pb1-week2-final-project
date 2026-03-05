import random

choices_per_question = 4

def unique(values):
    output = []
    seen = set()
    for v in values:
        if v is None:
            continue
        if isinstance(v, list):
            continue
        if v not in seen:
            seen.add(v)
            output.append(v)
    return output

def pick_wrong(correct, pool, f):
    pool = [y for y in pool if y != correct]
    random.shuffle(pool)
    return pool[:f]

def make_multi_choice(prompt, correct, wrong_pool, num_choices=choices_per_question, explanation=""):
    wrongs_needed = num_choices - 1
    wrongs = pick_wrong(correct, wrong_pool, wrongs_needed)
    if len(wrongs) < wrongs_needed:
        return None
    
    choices = [correct] + wrongs
    random.shuffle(choices)

    return {
        "prompt": prompt,
        "choices": choices,
        "answer_index": choices.index(correct),
        "explanation": explanation
    }

def generate_questions(lore, num_questions=10, num_choices=choices_per_question, seed=None):
    if seed is not None:
        random.seed(seed)
    
    entries = lore.get("entries", [])
    facts = lore.get("facts", {})

    if len(entries) < num_choices:
        raise ValueError(f"Need at least {num_choices} entries to generate multiple choice questions.")
    
    name_pool = unique([e.get("name") for e in entries])
    type_pool = unique([e.get("type") for e in entries])
    race_pool = unique([e.get("race") for e in entries])
    faction_pool = unique([e.get("faction") for e in entries])

    questions = []

    quiz_facts = lore.get("quiz_facts", [])
    pool_map = {
        "names": name_pool,
        "types": type_pool,
        "races": race_pool,
        "factions": faction_pool
    }

    for spec in quiz_facts:
        key = spec.get("key")
        prompt = spec.get("prompt")
        pool_name = spec.get("wrong_pool", "names")

        if not key or not prompt:
            continue

        if key in facts:
            correct = facts[key]
            wrong_pool = pool_map.get(pool_name, name_pool)

            q = make_multi_choice(
                prompt=prompt,
                correct=correct,
                wrong_pool=wrong_pool,
                num_choices=num_choices,
                explanation=f"(From lore facts: {key})"
            )
            if q:
                questions.append(q)

    if len(race_pool) >= choices_per_question:
        for e in entries:
            race = e.get("race")
            if race:
                q = make_multi_choice(
                    prompt=f"What race is {e['name']}?",
                    correct=race,
                    wrong_pool=race_pool,
                    num_choices=num_choices,
                    explanation=f"{e['name']} is {race}."
                )
                if q:
                    questions.append(q)

    if len(type_pool) >= choices_per_question:
        for e in entries:
            t = e.get("type")
            if t:
                q = make_multi_choice(
                    prompt=f"Which category best describes '{e['name']}'?",
                    correct=t,
                    wrong_pool=type_pool,
                    num_choices=num_choices,
                    explanation=f"{e['name']} is categorized as {t}."
                )
                if q:
                    questions.append(q)

    for e in entries:
        creator = e.get("created_by")
        if creator:
            q = make_multi_choice(
                prompt=f"Who created '{e['name']}'?",
                correct=creator,
                wrong_pool=name_pool,
                num_choices=num_choices,
                explanation=f"{e['name']} was created by {creator}."
            )
            if q:
                questions.append(q)

    for e in entries:
        phrase = e.get("catchphrase")
        if phrase:
            q = make_multi_choice(
                prompt=f'Who says "{phrase}"?',
                correct=e["name"],
                wrong_pool=name_pool,
                num_choices=num_choices,
                explanation=f"{e['name']} is known for saying \"{phrase}\"."
            )
            if q:
                questions.append(q)

    for e in entries:
        desc = (e.get("description") or "").strip()
        if len(desc) >= 35:
            q = make_multi_choice(
                prompt="Which entry matches this description?\n" + desc,
                correct=e["name"],
                wrong_pool=name_pool,
                num_choices=num_choices,
                explanation=f"The description refers to {e['name']}."
            )
            if q:
                questions.append(q)

    random.shuffle(questions)

    if not questions:
        raise ValueError("No questions could be generated from this lore file.")

    return questions[: min(num_questions, len(questions))]