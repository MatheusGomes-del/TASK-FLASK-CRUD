from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)


tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", "")) 
    task_id_control += 1
    tasks.append(new_task)
    print(data)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }

    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task_by_id = next((task for task in tasks if task.id == id), None)
    print(task_by_id)

    if task_by_id:
        return jsonify(task_by_id.to_dict())
    else:
        return jsonify({"message": "Não foi possível encontrar a tarefa"}), 404


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task_by_id = next((task for task in tasks if task.id == id), None)
    print(task_by_id)
    data = request.get_json()

    if task_by_id:
        task_by_id.title = data["title"]
        task_by_id.description = data["description"]
        task_by_id.completed = data["completed"] 
    

        return jsonify({"message": "Tarefa atualizada com sucesso"})
    else:
        return jsonify({"message": "Não foi possível encontrar a tarefa"}), 404



if __name__ == "__main__":
    app.run(debug=True)