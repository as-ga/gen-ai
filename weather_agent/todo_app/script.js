document.addEventListener("DOMContentLoaded", () => {
  const todoInput = document.getElementById("todo-input");
  const addButton = document.getElementById("add-button");
  const todoList = document.getElementById("todo-list");
  let todos = JSON.parse(localStorage.getItem("todos")) || [];
  function saveTodos() {
    localStorage.setItem("todos", JSON.stringify(todos));
  }
  function renderTodos() {
    todoList.innerHTML = "";
    todos.forEach((todo, index) => {
      const li = document.createElement("li");
      li.className = todo.completed ? "completed" : "";
      li.innerHTML =
        "sspan>" +
        todo.text +
        "</span>" +
        `<button class="complete-button" data-index="${index}">${
          todo.completed ? "Undo" : "Complete"
        }</button>` +
        `<button class="delete-button" data-index="${index}">Delete</button>`;
      todoList.appendChild(li);
    });
  }
  function addTodo() {
    const todoText = todoInput.value.trim();
    if (todoText !== "") {
      todos.push({ text: todoText, completed: false });
      todoInput.value = "";
      saveTodos();
      renderTodos();
    }
  }
  function toggleComplete(index) {
    todos[index].completed = !todos[index].completed;
    saveTodos();
    renderTodos();
  }
  function deleteTodo(index) {
    todos.splice(index, 1);
    saveTodos();
    renderTodos();
  }
  addButton.addEventListener("click", addTodo);
  todoInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      addTodo();
    }
  });
  todoList.addEventListener("click", (e) => {
    if (e.target.classList.contains("complete-button")) {
      const index = e.target.dataset.index;
      toggleComplete(index);
    }
    if (e.target.classList.contains("delete-button")) {
      const index = e.target.dataset.index;
      deleteTodo(index);
    }
  });
  renderTodos();
});
