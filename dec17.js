const fs = require('fs');
const path = require('path');
const readline = require('readline');

/**
 * Big Project: Simple Task Manager CLI App
 * Features:
 * - Add tasks
 * - List tasks
 * - Mark tasks as done
 * - Delete tasks
 * - Persist tasks to a JSON file
 */


const DATA_FILE = path.join(__dirname, 'tasks.json');

function loadTasks() {
    if (!fs.existsSync(DATA_FILE)) return [];
    return JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
}

function saveTasks(tasks) {
    fs.writeFileSync(DATA_FILE, JSON.stringify(tasks, null, 2));
}

function printTasks(tasks) {
    if (tasks.length === 0) {
        console.log('No tasks found.');
        return;
    }
    tasks.forEach((task, idx) => {
        console.log(
            `${idx + 1}. [${task.done ? 'x' : ' '}] ${task.text}`
        );
    });
}

function prompt() {
    return readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
}

function mainMenu() {
    const rl = prompt();
    console.log('\nTask Manager');
    console.log('1. List tasks');
    console.log('2. Add task');
    console.log('3. Mark task as done');
    console.log('4. Delete task');
    console.log('5. Exit');
    rl.question('Choose an option: ', answer => {
        rl.close();
        handleMenu(answer.trim());
    });
}

function handleMenu(choice) {
    let tasks = loadTasks();
    switch (choice) {
        case '1':
            printTasks(tasks);
            mainMenu();
            break;
        case '2':
            addTask(tasks);
            break;
        case '3':
            markTaskDone(tasks);
            break;
        case '4':
            deleteTask(tasks);
            break;
        case '5':
            console.log('Goodbye!');
            process.exit(0);
        default:
            console.log('Invalid option. Please try again.');
            mainMenu();
    }
}

function addTask(tasks) {
    const rl = prompt();
    rl.question('Enter task description: ', desc => {
        if (desc.trim() === '') {
            console.log('Task cannot be empty, try again.');
        } else {
            tasks.push({ text: desc.trim(), done: false });
            saveTasks(tasks);
            console.log('Task added.');
        }
        rl.close();
        mainMenu();
    });
}

function markTaskDone(tasks) {
    if (tasks.length === 0) {
        console.log('No tasks to mark.');
        return mainMenu();
    }
    printTasks(tasks);
    const rl = prompt();
    rl.question('Enter the amount task number to mark as done: ', num => {
        const idx = parseInt(num) - 1;
        if (isNaN(idx) || idx < 0 || idx >= tasks.length) {
            console.log('Invalid task number.');
        } else {
            tasks[idx].done = true;
            saveTasks(tasks);
            console.log('Task marked as done.');
        }
        rl.close();
        mainMenu();
    });
}

function deleteTask(tasks) {
    if (tasks.length === 0) {
        console.log('No tasks to delete.');
        return mainMenu();
    }
    printTasks(tasks);
    const rl = prompt();
    rl.question('Enter task number to delete: ', num => {
        const idx = parseInt(num) - 1;
        if (isNaN(idx) || idx < 0 || idx >= tasks.length) {
            console.log('Invalid task number.');
        } else {
            tasks.splice(idx, 1);
            saveTasks(tasks);
            console.log('Task deleted.');
        }
        rl.close();
        mainMenu();
    });
}

// Start the app
mainMenu();