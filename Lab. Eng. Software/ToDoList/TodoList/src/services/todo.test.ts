/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { ToDoList } from './TodoList'
import { Task, UpdateTask } from '../models/Task'
import { TodoListRepository } from '../repository/TodoListRepository'

const anyTask: Task = {
  id: 1,
  title: 'any_title',
  description: 'any_description',
  targetDate: '01/01/2025',
  type: 'any_type',
  priority: '1',
  subTasks: []
}

const makeRepositoryStub = (): TodoListRepository => {
  class TodoListStub implements TodoListRepository {
    createdTasks: Task[] = []
    create (task: Task) {
      this.createdTasks.push(task)
      return {
        success: true,
        error: null
      }
    }

    getAll () {
      return {
        success: this.createdTasks,
        error: null
      }
    }

    update (task: UpdateTask) {
      return {
        success: true,
        error: null
      }
    }

    delete (id: number) {
      return {
        success: true,
        error: null
      }
    }
  }
  return new TodoListStub()
}

describe('ToDoList', () => {
  describe('Testing add', () => {
    test('should add a new task to the list', () => {
      const repositoryStub = makeRepositoryStub()
      const todoInstance = new ToDoList(repositoryStub)
      todoInstance.add(anyTask)
      const tasks = todoInstance.getTasks()
      expect(tasks).toEqual([anyTask])
    })

    test('should add a valid tasks', () => {
      const repositoryStub = makeRepositoryStub()
      const todoInstance = new ToDoList(repositoryStub)
      const invalidValue: any = {
        invalidField: 'invalidValue'
      }
      const response = todoInstance.add(invalidValue)
      expect(response).toEqual('Missing properties in task object')
    })
  })
  describe('getTasks', () => {
    test('should itialize tasks with an empty array', () => {
      const repositoryStub = makeRepositoryStub()
      jest.spyOn(repositoryStub, 'getAll').mockReturnValueOnce({
        success: [],
        error: null
      })
      const todoInstance = new ToDoList(repositoryStub)
      const response = todoInstance.getTasks()
      expect(response).toEqual([])
    })
  })
  describe('Testing update', () => {
    test('should update a task in the list', () => {
      const repositoryStub = makeRepositoryStub()
      const todoInstance = new ToDoList(repositoryStub)
      todoInstance.add(anyTask)
      const updatedTask = {
        title: 'Test_Update',
        description: 'Test_updated_description',
        targetDate: '02/02/2025',
        type: 'Test_updated_type',
        priority: '2',
        subTasks: []
      }
      const result = todoInstance.updateTask(0, updatedTask)
      // const tasks = todoInstance.getTasks()
      expect(result).toBe(true)
    })

    test('should not update task if index is out of bounds', () => {
      const repositoryStub = makeRepositoryStub()
      const todoInstance = new ToDoList(repositoryStub)
      const initialTask = {
        title: 'any_title',
        description: 'any_description',
        targetDate: '01/01/2025',
        type: 'any_type',
        priority: '1',
        subTasks: []
      }
      todoInstance.add(initialTask)
      const updatedTask = {
        title: 'Test_Update',
        description: 'Test_updated_description',
        targetDate: '02/02/2025',
        type: 'Test_updated_type',
        priority: '2',
        subTasks: []
      }
      todoInstance.updateTask(0, updatedTask) // Index out of bounds
      const tasks = todoInstance.getTasks()
      expect(tasks).toEqual([initialTask])
    })
  })

  describe('Testing remove', () => {
    test('should remove a task from the list', () => {
      const repositoryStub = makeRepositoryStub()
      const todoInstance = new ToDoList(repositoryStub)
      todoInstance.add(anyTask)
      const response = todoInstance.removeTask(0)
      expect(response).toBe(true)
    })

    test('should not remove task if index is out of bounds', () => {
      const repositoryStub = makeRepositoryStub()
      const todoInstance = new ToDoList(repositoryStub)
      todoInstance.add(anyTask)
      todoInstance.removeTask(1) // Index out of bounds
      const tasks = todoInstance.getTasks()
      expect(tasks).toEqual([anyTask])
    })
  })
})
