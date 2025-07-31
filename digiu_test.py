import streamlit as st

# Core Interaction Dimensions (CIDs)
cids = {
    'CID1': {'name': 'Expressiveness', 'poles': 'E ↔ G', 'description': 'Expressive vs. Guarded'},
    'CID2': {'name': 'Reactivity', 'poles': 'R ↔ A', 'description': 'Reactive vs. Anticipative'},
    'CID3': {'name': 'Tone Sensitivity', 'poles': 'T ↔ F', 'description': 'Tone-focused vs. Factual'},
    'CID4': {'name': 'Frequency', 'poles': 'F ↔ I', 'description': 'Frequent vs. Infrequent communicator'},
    'CID5': {'name': 'Linearity', 'poles': 'L ↔ C', 'description': 'Linear vs. Chaotic in communication'},
    'CID6': {'name': 'Discretion', 'poles': 'D ↔ S', 'description': 'Discreet vs. Sharing-oriented'},
    'CID7': {'name': 'Internalization', 'poles': 'I ↔ E', 'description': 'Internalizes vs. Emotionally reactive'}
}

# Personality types
personality_types = {
    "Echo Reactor": {
        "description": (
            "Echo Reactors are emotionally expressive and highly reactive to digital interactions. "
            "They thrive on immediate feedback, often using emojis, voice notes, and quick replies to convey feelings. "
            "Their digital presence is characterized by high engagement and tone sensitivity.\n\n"
            "These individuals feel deeply connected to their digital interactions and may experience "
            "emotional highs and lows based on responses. They maintain constant availability and "
            "express themselves vividly through digital channels."
        )
    },
    "Structured Strategist": {
        "description": (
            "Structured Strategists approach digital communication with organization and purpose. "
            "They value clarity, professionalism, and intentional tone in all interactions. "
            "Their communication style is linear, composed, and carefully planned.\n\n"
            "These individuals maintain clear boundaries between different types of communication "
            "and prefer scheduled interactions over spontaneous exchanges. They edit messages for "
            "precision and typically avoid emotional or casual digital expressions."
        )
    },
    "Streaming Storyteller": {
        "description": (
            "Streaming Storytellers are expressive sharers who engage through vivid digital narratives. "
            "They excel at visual communication, using stories, tags, filters, and multimedia content "
            "to create compelling digital personas.\n\n"
            "These individuals view digital platforms as stages for self-expression and connection. "
            "They frequently update their online presence and enjoy crafting engaging content that "
            "reflects their experiences and personality."
        )
    },
    "Gentle Ghost": {
        "description": (
            "Gentle Ghosts are quiet observers in the digital landscape. They maintain minimalistic "
            "online presences, rarely initiating interactions or sharing personal content. "
            "Their communication style is reserved, delayed, and often concise.\n\n"
            "These individuals prefer listening to participating and value digital solitude. "
            "They carefully curate their limited online interactions and often disable notifications "
            "to maintain their peaceful digital existence."
        )
    },
    "Notification Nomad": {
        "description": (
            "Notification Nomads are agile digital multitaskers who navigate multiple platforms simultaneously. "
            "Their communication is quick but scattered, often characterized by rapid context-switching "
            "and intermittent engagement.\n\n"
            "These individuals maintain high digital mobility but may miss details due to their "
            "fragmented attention. They respond promptly but superficially, constantly balancing "
            "multiple conversation threads across various platforms."
        )
    },
    "Compartmentalized Connector": {
        "description": (
            "Compartmentalized Connectors strategically segment their digital interactions based on context. "
            "They maintain distinct communication styles for professional, casual, and private spheres, "
            "switching seamlessly between personas.\n\n"
            "These individuals are highly aware of digital boundaries and context appropriateness. "
            "They carefully manage different aspects of their digital identity, maintaining clear "
            "separation between various relationship circles and communication purposes."
        )
    }
}

# Questions with CID impacts
questions = [
    {
        "question": "How do you feel when someone sends you a long voice note?",
        "answers": [
            {"text": "Excited! I love hearing people explain in detail.", "impact": {"CID1": 2, "CID3": 2, "CID4": 1}},
            {"text": "Fine, I'll usually listen and maybe skim.", "impact": {"CID1": 0, "CID3": 0, "CID4": 0}},
            {"text": "Annoyed — I wish they'd text instead.", "impact": {"CID1": -1, "CID3": -1, "CID4": -1}},
            {"text": "I often skip them entirely.", "impact": {"CID1": -2, "CID3": -2, "CID4": -2}}
        ]
    },
    {
        "question": "How do you usually save contacts on your phone?",
        "answers": [
            {"text": "Full name, formal.", "impact": {"CID1": -1, "CID5": 1, "CID6": 1}},
            {"text": "Nicknames or funny names.", "impact": {"CID1": 2, "CID5": -1, "CID6": -1}},
            {"text": "Just first names.", "impact": {"CID1": 0, "CID5": 0, "CID6": 0}}
        ]
    },
    {
        "question": "How do you react when someone doesn't reply quickly?",
        "answers": [
            {"text": "I feel a little anxious or ignored.", "impact": {"CID2": 2, "CID7": 2}},
            {"text": "I try not to overthink it.", "impact": {"CID2": 0, "CID7": 0}},
            {"text": "I don't notice or care.", "impact": {"CID2": -2, "CID7": -2}},
            {"text": "I may insist.", "impact": {"CID2": 1, "CID7": 1}}
        ]
    },
    {
        "question": "How quickly do you usually reply to messages?",
        "answers": [
            {"text": "Immediately — I feel bad if I don't.", "impact": {"CID2": 2, "CID4": 2, "CID7": 1}},
            {"text": "Within a few hours.", "impact": {"CID2": 0, "CID4": 0, "CID7": 0}},
            {"text": "When I feel like it.", "impact": {"CID2": -1, "CID4": -1, "CID7": -1}},
            {"text": "I often forget.", "impact": {"CID2": -2, "CID4": -2, "CID7": -2}}
        ]
    },
    {
        "question": "Do you edit a message for spelling/grammar after sending it?",
        "answers": [
            {"text": "Yes, always.", "impact": {"CID3": 2, "CID5": 1}},
            {"text": "Only if formal.", "impact": {"CID3": 0, "CID5": 0}},
            {"text": "No — I leave it if can be understood.", "impact": {"CID3": -1, "CID5": -1}}
        ]
    },
    {
        "question": "Do you re-read your old conversations?",
        "answers": [
            {"text": "Yes — I enjoy reliving moments.", "impact": {"CID1": 1, "CID7": 1}},
            {"text": "Only if I need context.", "impact": {"CID1": 0, "CID7": 0}},
            {"text": "No — I move on.", "impact": {"CID1": -1, "CID7": -1}}
        ]
    },
    {
        "question": "Do you listen to your own voice notes after sending them?",
        "answers": [
            {"text": "Always — to check how I sound.", "impact": {"CID1": 2, "CID3": 2, "CID7": 1}},
            {"text": "Sometimes.", "impact": {"CID1": 0, "CID3": 0, "CID7": 0}},
            {"text": "Never.", "impact": {"CID1": -1, "CID3": -1, "CID7": -1}}
        ]
    },
    {
        "question": "How do you react to reels/memes you receive?",
        "answers": [
            {"text": "I always react with emojis/comments", "impact": {"CID1": 2, "CID2": 1, "CID6": 1}},
            {"text": "React only if I find the content funny/engaging.", "impact": {"CID1": 0, "CID2": 0, "CID6": 0}},
            {"text": "Mostly laugh silently and don't reply.", "impact": {"CID1": -1, "CID2": -1, "CID6": -1}},
            {"text": "Ignore them.", "impact": {"CID1": -2, "CID2": -2, "CID6": -2}}
        ]
    },
    {
        "question": "What best describes your emoji/sticker use?",
        "answers": [
            {"text": "Very expressive — I use them often.", "impact": {"CID1": 2, "CID3": 1}},
            {"text": "Minimal or none.", "impact": {"CID1": -2, "CID3": -1}},
            {"text": "Only in casual chats (context based).", "impact": {"CID1": 0, "CID3": 0}}
        ]
    },
    {
        "question": "How often do you delete/re-edit your stories?",
        "answers": [
            {"text": "Often — I overthink them.", "impact": {"CID3": 2, "CID7": 2}},
            {"text": "Sometimes.", "impact": {"CID3": 0, "CID7": 0}},
            {"text": "Never.", "impact": {"CID3": -1, "CID7": -1}}
        ]
    },
    {
        "question": "Do you check who views/reacts to your stories?",
        "answers": [
            {"text": "Always.", "impact": {"CID2": 2, "CID7": 1}},
            {"text": "Sometimes.", "impact": {"CID2": 0, "CID7": 0}},
            {"text": "Never.", "impact": {"CID2": -1, "CID7": -1}}
        ]
    },
    {
        "question": "Do you feel pressured to reply to one person on multiple platforms at once?",
        "answers": [
            {"text": "Yes, I try to keep up everywhere and all the time.", "impact": {"CID2": 2, "CID4": 2, "CID5": -2}},
            {"text": "Only if I have time.", "impact": {"CID2": 0, "CID4": 0, "CID5": 0}},
            {"text": "No, I respond on my own time.", "impact": {"CID2": -1, "CID4": -1, "CID5": 1}}
        ]
    },
    {
        "question": "Do you check if someone saw your message (blue ticks)?",
        "answers": [
            {"text": "Yes, obsessively.", "impact": {"CID2": 2, "CID7": 2}},
            {"text": "Sometimes.", "impact": {"CID2": 0, "CID7": 0}},
            {"text": "I don't care.", "impact": {"CID2": -2, "CID7": -2}}
        ]
    },
    {
        "question": "Do you allow people to see when you've read their messages (e.g., blue ticks)?",
        "answers": [
            {"text": "Yes, I don't mind people knowing I saw it.", "impact": {"CID6": -1, "CID7": -1}},
            {"text": "No, I turn that setting off.", "impact": {"CID6": 2, "CID7": 1}},
            {"text": "It depends on the app.", "impact": {"CID6": 0, "CID7": 0}}
        ]
    },
    {
        "question": "Do you usually respond to messages while busy (in class, meetings, etc.)?",
        "answers": [
            {"text": "Yes, I feel the need to stay connected.", "impact": {"CID2": 2, "CID4": 2, "CID5": -1}},
            {"text": "Only if it's urgent or from someone important.", "impact": {"CID2": 0, "CID4": 0, "CID5": 0}},
            {"text": "No, I wait until I'm free.", "impact": {"CID2": -1, "CID4": -1, "CID5": 1}}
        ]
    },
    {
        "question": "Do you prepare your message drafts or rehearse before sending?",
        "answers": [
            {"text": "Yes, I even retype or record more than once.", "impact": {"CID3": 2, "CID5": 1, "CID7": 1}},
            {"text": "Sometimes, if it's a sensitive conversation.", "impact": {"CID3": 0, "CID5": 0, "CID7": 0}},
            {"text": "No, I go with what comes naturally.", "impact": {"CID3": -1, "CID5": -1, "CID7": -1}}
        ]
    },
    {
        "question": "Do you edit social media posts after publishing?",
        "answers": [
            {"text": "Yes, constantly. I want everything to look right.", "impact": {"CID3": 2, "CID7": 1}},
            {"text": "Sometimes, if I notice something off.", "impact": {"CID3": 0, "CID7": 0}},
            {"text": "No, I usually post and leave it.", "impact": {"CID3": -1, "CID7": -1}}
        ]
    },
    {
        "question": "How often do you feel anxious when someone takes a long time to respond?",
        "answers": [
            {"text": "Very often — I keep checking.", "impact": {"CID2": 2, "CID7": 2}},
            {"text": "Sometimes — I try to distract myself.", "impact": {"CID2": 0, "CID7": 0}},
            {"text": "Rarely — I don't mind waiting.", "impact": {"CID2": -1, "CID7": -1}}
        ]
    },
    {
        "question": "How do you behave in group chats?",
        "answers": [
            {"text": "I'm active — always commenting or reacting.", "impact": {"CID1": 2, "CID4": 1, "CID6": -1}},
            {"text": "I observe mostly, but participate occasionally.", "impact": {"CID1": 0, "CID4": 0, "CID6": 0}},
            {"text": "I rarely or never write, but read everything.", "impact": {"CID1": -1, "CID4": -1, "CID6": 1}},
            {"text": "I mute or leave most groups.", "impact": {"CID1": -2, "CID4": -2, "CID6": 2}}
        ]
    },
    {
        "question": "What kind of stickers or emoji do you tend to use?",
        "answers": [
            {"text": "Funny or absurd ones — I like to surprise people.", "impact": {"CID1": 2, "CID3": 1}},
            {"text": "Classic smileys, hearts, and common icons.", "impact": {"CID1": 0, "CID3": 0}},
            {"text": "Reaction gifs or memes.", "impact": {"CID1": 1, "CID3": 1}},
            {"text": "I don't use stickers or emojis much.", "impact": {"CID1": -2, "CID3": -1}}
        ]
    },
    {
        "question": "How do you usually reply to long messages?",
        "answers": [
            {"text": "With equal length and detail.", "impact": {"CID1": 1, "CID3": 1, "CID5": 1}},
            {"text": "Summarized, to the point.", "impact": {"CID1": -1, "CID3": -1, "CID5": 0}},
            {"text": "With emojis or brief responses.", "impact": {"CID1": 1, "CID3": 0, "CID5": -1}}
        ]
    },
    {
        "question": "Do you like to see your own previous comments in chats?",
        "answers": [
            {"text": "Yes, I scroll back and reflect on them.", "impact": {"CID3": 1, "CID7": 1}},
            {"text": "Sometimes — if I'm proud of something I said.", "impact": {"CID3": 0, "CID7": 0}},
            {"text": "Not really — I rarely revisit past chats.", "impact": {"CID3": -1, "CID7": -1}}
        ]
    },
    {
        "question": "How do you manage notifications?",
        "answers": [
            {"text": "I check and clear everything immediately.", "impact": {"CID2": 2, "CID4": 2, "CID5": -1}},
            {"text": "I leave them until I'm ready to check.", "impact": {"CID2": 0, "CID4": 0, "CID5": 0}},
            {"text": "I often let them pile up.", "impact": {"CID2": -1, "CID4": -1, "CID5": -1}},
            {"text": "I disable most notifications.", "impact": {"CID2": -2, "CID4": -2, "CID5": 1}}
        ]
    },
    {
        "question": "When someone tags you in a story or post, how do you react?",
        "answers": [
            {"text": "I repost it or react immediately.", "impact": {"CID1": 2, "CID6": -2}},
            {"text": "I reply privately, if needed.", "impact": {"CID1": 0, "CID6": 0}},
            {"text": "I usually ignore or hide it.", "impact": {"CID1": -1, "CID6": 1}}
        ]
    },
    {
        "question": "Do you enjoy customizing your phone or apps (themes, layouts, etc.)?",
        "answers": [
            {"text": "Yes, I regularly change how it looks.", "impact": {"CID1": 2, "CID6": -1}},
            {"text": "Sometimes — I personalize small things.", "impact": {"CID1": 0, "CID6": 0}},
            {"text": "No, I leave everything mostly on default.", "impact": {"CID1": -1, "CID6": 1}}
        ]
    },
    {
        "question": "How often do you feel the need to be reachable at all times?",
        "answers": [
            {"text": "Always — I hate being disconnected.", "impact": {"CID2": 2, "CID4": 2, "CID7": 1}},
            {"text": "Sometimes — depending on the day.", "impact": {"CID2": 0, "CID4": 0, "CID7": 0}},
            {"text": "Rarely — I like to unplug.", "impact": {"CID2": -1, "CID4": -1, "CID7": -1}}
        ]
    },
    {
        "question": "What role do memes play in your digital identity?",
        "answers": [
            {"text": "A big one — I express myself through memes.", "impact": {"CID1": 2, "CID3": 1, "CID6": -1}},
            {"text": "Somewhat — I share memes occasionally.", "impact": {"CID1": 0, "CID3": 0, "CID6": 0}},
            {"text": "Minimal — I mostly just view them.", "impact": {"CID1": -1, "CID3": -1, "CID6": 1}},
            {"text": "None — I don't really follow memes.", "impact": {"CID1": -2, "CID3": -2, "CID6": 1}}
        ]
    },
    {
        "question": "Do you ever reread or relisten to things you've sent just to see how others might perceive them?",
        "answers": [
            {"text": "Yes — I do this often.", "impact": {"CID3": 2, "CID7": 2}},
            {"text": "Sometimes, if it was a big deal.", "impact": {"CID3": 0, "CID7": 0}},
            {"text": "No — I don't worry about it.", "impact": {"CID3": -1, "CID7": -1}}
        ]
    }
]

def calculate_personality(scores):
    """Determine personality based on CID scores"""
    # Define personality thresholds
    if scores['CID1'] > 5 and scores['CID2'] > 4 and scores['CID3'] > 4:
        return "Echo Reactor"
    elif scores['CID5'] > 5 and scores['CID1'] < 0 and scores['CID3'] < 0:
        return "Structured Strategist"
    elif scores['CID1'] > 5 and scores['CID6'] < -3 and scores['CID4'] > 4:
        return "Streaming Storyteller"
    elif scores['CID4'] < -5 and scores['CID1'] < -3 and scores['CID2'] < -3:
        return "Gentle Ghost"
    elif scores['CID2'] > 4 and scores['CID5'] < -4 and scores['CID4'] > 4:
        return "Notification Nomad"
    else:
        return "Compartmentalized Connector"

def main():
    st.set_page_config(page_title="DigiU Digital Personality Test", layout="wide")
    
    # Initialize session state
    if 'current_q' not in st.session_state:
        st.session_state.current_q = 0
        st.session_state.scores = {cid: 0 for cid in cids}
        st.session_state.completed = False
        st.session_state.personality = ""
    
    # Header
    st.title("DigiU Digital Personality Test")
    st.markdown("Discover your digital communication style with our 28-question assessment")
    
    # Test in progress
    if not st.session_state.completed and st.session_state.current_q < len(questions):
        current_question = questions[st.session_state.current_q]
        
        # Show progress
        progress = st.session_state.current_q / len(questions)
        st.progress(progress)
        st.subheader(f"Question {st.session_state.current_q + 1}/{len(questions)}")
        st.markdown(f"**{current_question['question']}**")
        
        # Display answers
        for i, answer in enumerate(current_question['answers']):
            if st.button(answer['text'], key=f"q{st.session_state.current_q}a{i}"):
                # Update scores
                for cid, value in answer['impact'].items():
                    st.session_state.scores[cid] += value
                
                # Move to next question
                st.session_state.current_q += 1
                if st.session_state.current_q >= len(questions):
                    st.session_state.completed = True
                    st.session_state.personality = calculate_personality(st.session_state.scores)
                # FIX: Use st.rerun() instead of experimental_rerun
                st.rerun()
    
    # Show results
    elif st.session_state.completed:
        st.balloons()
        st.subheader("Your Digital Personality Type Is")
        st.markdown(f"# {st.session_state.personality}")
        st.markdown("---")
        st.write(personality_types[st.session_state.personality]['description'])
        
        st.markdown("---")
        st.subheader("Your Core Interaction Dimensions")
        col1, col2 = st.columns(2)
        for i, (cid, score) in enumerate(st.session_state.scores.items()):
            col = col1 if i % 2 == 0 else col2
            col.metric(f"{cids[cid]['name']} ({cids[cid]['poles']})", 
                      f"{score} points", 
                      help=cids[cid]['description'])
        
        if st.button("Retake Test"):
            st.session_state.current_q = 0
            st.session_state.scores = {cid: 0 for cid in cids}
            st.session_state.completed = False
            st.session_state.personality = ""
            # FIX: Use st.rerun() instead of experimental_rerun
            st.rerun()

if __name__ == "__main__":
    main()