// title
// description
// target
// type
// prioridade
// subtask

type Task = {
    title: string,
    description: string,
    type: string,
    priority?: string,
    subtasks?: Task[]
}
export class ToDoList {
    private tasks: Task[] = []

    add(task: Task) {
        this.tasks.push(task)
    }
}