import { TodoListRepository } from '../repository/TodoListRepository'

export type Task = {
  title: string,
  description: string,
  targetDate: string,
  type?: string,
  priority?: string,
  subTasks?: Task[]
}

export type UpdateTask = {
  title?: string,
  description?: string,
  targetDate?: string,
  type?: string,
  priority?: string,
  subTasks?: Task[]
}

export class ToDoList {
  private tasks: Task[] = []
  private repository: TodoListRepository

  constructor (repository: TodoListRepository) {
    this.repository = repository
  }

  add (task: Task) {
    const missingProperties = ['title', 'description', 'targetDate'].filter(
      (prop) => !Object.keys(task).includes(prop)
    )
    try {
      if (missingProperties.length > 0) {
        return 'Missing properties in task object'
      }

      const response = this.repository.create(task)
      if (response.error) {
        return 'Falha ao criar tarefa'
      }
      return 'Tarefa criada com sucesso'
    } catch (error) {
      return new Error(JSON.stringify(error))
    }
  }

  getTasks () {
    const response = this.repository.getAll()
    if (response.error) {
      return 'Falha ao listar tarefas'
    }
    return response.success
  }

  updateTask (index: number, task: UpdateTask): boolean {
    if (index < 0 || index > this.tasks.length) {
      throw new Error('Index out of bounds')
    }

    // Atualiza a tarefa apenas se todos os campos fornecidos forem válidos
    const updatedTask = { ...this.tasks[index], ...task }
    const missingProperties = ['title', 'description', 'targetDate'].filter(
      prop => !(prop in updatedTask)
    )

    if (missingProperties.length > 0) {
      throw new Error('Missing properties in updated task object')
    }

    this.tasks[index] = updatedTask
    return true
  }

  removeTask (index: number) {
    try {
      this.tasks.splice(index, 1)
      return true
    } catch (error) {
      return false
    }
  }
}
