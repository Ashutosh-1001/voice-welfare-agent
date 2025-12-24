from agent.planner import plan
from agent.executor import check_scheme
from agent.checker import final_answer
import memory

user_text = "నాకు ప్రభుత్వ పథకం కావాలి"

decision = plan(user_text, memory.memory)

if decision == "ASK_AGE":
    print("Agent: మీ వయస్సు చెప్పండి")
    memory.save("age", 25)

decision = plan(user_text, memory.memory)

if decision == "ASK_INCOME":
    print("Agent: మీ ఆదాయం చెప్పండి")
    memory.save("income", 150000)

decision = plan(user_text, memory.memory)

if decision == "CHECK_SCHEME":
    result = check_scheme(memory.get("age"), memory.get("income"))
    print("Agent:", final_answer(result))
