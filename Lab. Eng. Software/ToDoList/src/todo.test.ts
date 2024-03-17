/* eslint-disable @typescript-eslint/no-explicit-any */
import { ToDoList } from './TodoList'

const anyTask = {
  title: 'any_title',
  description: 'any_description',
  targetDate: '01/01/2025',
  type: 'any_type',
  priority: '1',
  subTasks: []
}

describe('ToDoList', () => {
  describe('Testing add', () => {
    test('should add a new task to the list', () => {
      const todoInstance = new ToDoList()
      todoInstance.add(anyTask)
      const tasks = todoInstance.getTasks()
      expect(tasks).toEqual([anyTask])
    })

    test('should add a valid tasks', () => {
      const todoInstance = new ToDoList()
      const invalidValue: any = {
        invalidField: 'invalidValue'
      }
      todoInstance.add(invalidValue)
      const tasks = todoInstance.getTasks()
      expect(tasks).toEqual([])
    })
  })
})
describe('Testing update', () => {
  test('should update a task in the list', () => {
    const todoInstance = new ToDoList()
    todoInstance.add(anyTask)
    const updatedTask = {
      title: 'Test_Update',
      description: 'Test_updated_description',
      targetDate: '02/02/2025',
      type: 'Test_updated_type',
      priority: '2',
      subTasks: []
    }
    todoInstance.updateTask(0, updatedTask)
    const tasks = todoInstance.getTasks()
    expect(tasks).toEqual([updatedTask])
  })

  test('should not update task if index is out of bounds', () => {
    const todoInstance = new ToDoList()
    const anyTask = {
      title: 'any_title',
      description: 'any_description',
      targetDate: '01/01/2025',
      type: 'any_type',
      priority: '1',
      subTasks: []
    }
    todoInstance.add(anyTask)
    const updatedTask = {
      title: 'Test_Update',
      description: 'Test_updated_description',
      targetDate: '02/02/2025',
      type: 'Test_updated_type',
      priority: '2',
      subTasks: []
    }
    todoInstance.updateTask(1, updatedTask) // Index out of bounds
    const tasks = todoInstance.getTasks()
    expect(tasks).toEqual([anyTask])
  })
})

describe('Testing remove', () => {
  test('should remove a task from the list', () => {
    const todoInstance = new ToDoList()
    todoInstance.add(anyTask)
    todoInstance.removeTask(0)
    const tasks = todoInstance.getTasks()
    expect(tasks).toEqual([])
  })

  test('should not remove task if index is out of bounds', () => {
    const todoInstance = new ToDoList()
    todoInstance.add(anyTask)
    todoInstance.removeTask(1) // Index out of bounds
    const tasks = todoInstance.getTasks()
    expect(tasks).toEqual([anyTask])
  })
})
