import random
from datetime import date
# Agent Data
agent1 = {'id': 1, 'is_available': True, 'available_since': date(2019, 7, 2), 'role': ['spanish', 'sales']}
agent2 = {'id': 2, 'is_available': True, 'available_since': date(2020, 3, 2), 'role': ['sales', 'support', 'spanish']}
agent3 = {'id': 3, 'is_available': False, 'available_since': date(2020, 4, 23), 'role': ['spanish','sales']}
agent4 = {'id': 4, 'is_available': True, 'available_since': date(2020, 5, 12), 'role': ['support','sales']}
agent5 = {'id': 5, 'is_available': True, 'available_since': date(2020, 7, 9), 'role': ['spanish','sales','support']}

# List of all agents present
agents = [agent1, agent2, agent3, agent4, agent5]

# Code for mode : all available
def mode1(rel_agents):
    final_agent = []
    for i in rel_agents:
        final_agent.append(i['id'])
    return ["agent" + str(x) for x in final_agent]

# Code for mode : least busy
def mode2(rel_agents):
    current_date = date.today()
    max = -1
    for x in rel_agents:
        value = (current_date - x['available_since']).days
        if value > max:
            max = value
            final_agent = x['id']
    return "agent" + str(final_agent)

# Code for mode : random
def mode3(rel_agents):
    final_agent = (random.choice(rel_agents))['id']
    return "agent" + str(final_agent)



def agent_selector(agents, sel_mode, issue) :

# List of all the related agents for the issue came (contains all the agent that are available and has the same roles the issue contains
    rel_agents = []
    for i in range(len(agents)):
        if (all(x in agents[i]['role'] for x in issue)) and agents[i]['is_available'] :
            rel_agents.append(agents[i])

# If there is no agent related to that issue
    if not rel_agents :
        return "There Is No Agent Related to Your Issue"

#   Mode 1 : (all available)
    if sel_mode == 'all available':
        return mode1(rel_agents)

#   Mode 2 : (least busy)
    elif sel_mode == 'least busy':
        return mode2(rel_agents)

#   Mode 3 : (random)
    elif sel_mode == 'random':
        return mode3(rel_agents)

# If user chooses a different mode than available
    else:
        return "Please Enter A Correct Mode"

# Issue that has come
issue = input('Please Tell Your Issue (What kind of agent you want to higher :\n').split()

# Mode of selection that user will choose
sel_mode = input('Choose A Selection Mode :\nall available\nleast busy\nrandom\n')
print(f'Here Is The List Of Agents That can Handle Your Issue:')

# List of agents that are going to present to user
agents_to_present = agent_selector(agents, sel_mode, issue)

print(agents_to_present)


