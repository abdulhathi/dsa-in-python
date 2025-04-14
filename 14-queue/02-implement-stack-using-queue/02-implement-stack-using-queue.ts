class StackUsingQueue {
  q1 = []
  q2 = []
  constructor() {}

  push(val: number) {
    this.q2 = this.q1
    this.q1 = []
    this.q1.push(val)
    while (this.q2.length > 0) {
      this.q1.push(this.q2.shift())
    }
  }

  pop() {
    return this.q1 ? this.q1.shift() : null
  }

  peek() {
    return this.q1 ? this.q1[0] : null
  }

  size() {
    return this.q1.length
  }

  print() {
    const res = []
    for (let i = 0; i < this.q1.length; i++) {
      res.push(this.q1[i])
    }
    console.log(`[${res.join(',')}]`)
  }
}

const stack = new StackUsingQueue()
stack.push(10)
stack.push(20)
stack.push(30)

stack.print()
console.log(stack.pop())
console.log(stack.pop())
stack.print()
