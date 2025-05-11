Python design principles PEP20 - "The Zen of Python"

readability, simplicity, explicitness

Dynamic typing - type decided at runtime
Strong typing - operations on incompatible types cause errors

Interpreted language

.py to .pyc using interpreter (e.g. CPython)

.pyc runs on PVM (Python Virtual Machine)

Python implementations - CPython (written in C), PyPy (Just in time (JIT) compiler), Jython (JVM based), IronPython (for .NET framework)

Memory management

automatic memory management with garbage collection

refrence counting - Each object keeps track of how many references point to it. When the count drops to zero, the memory is reclaimed.

garbage collector (GC) - Handles cyclic references. Python’s gc module can manage and inspect this.

memory pools - uses its own memory allocator (e.g., PyMalloc in CPython) to optimize small object allocations.

**Heap memory - all Python objects and data structures are stored here
**Stack memory - Used for local variables and function call management.
**Global Interpreter Lock (GIL) - mutex in CPython to protect memory management. Limits true parallelism but simplifies thread safety.

Abstract Syntax Trees (ASTs):
Python code is parsed into an AST before bytecode compilation.
The ast module in Python allows you to inspect and manipulate this.
Dynamic Features:
Dynamic Attribute Creation: Add or modify attributes at runtime.
Duck Typing: Objects are checked for behavior (methods/attributes) rather than type.
Reflection: Access object information (e.g., using getattr, hasattr).

ython Standard Library & Built-ins
Standard Library: Comprehensive modules for file I/O, OS access, networking, data serialization, and more.
Built-in Functions: Functions like len(), type(), and map() are implemented in C for performance.
6. JIT Compilation and Optimization
Python itself doesn’t have native Just-In-Time (JIT) compilation, but alternatives like PyPy use JIT to optimize runtime performance.
Tools like Numba can JIT-compile Python functions for numerical computation.
7. Tools and Debugging
Disassembly:
Use the dis module to inspect Python bytecode.
Profiling:
Modules like cProfile and timeit for performance analysis.
Error Handling:
Learn exception hierarchies (BaseException, Exception, OSError, etc.).
8. Advanced Topics
Meta-programming:
Decorators: Modify functions or classes dynamically.
Metaclasses: Control class creation.
Concurrency:
Threads vs. Multiprocessing:
Use threading for I/O-bound tasks and multiprocessing for CPU-bound tasks.
Asyncio: Event-loop-based concurrency for handling asynchronous tasks.
C Extensions:
Write high-performance extensions in C (e.g., ctypes, Cython, or writing CPython modules directly).
9. How Python Works with Other Languages
JDK (for Jython):
Jython allows Python code to interact with Java classes and libraries.
C/C++:
CPython integrates seamlessly with C/C++ via the C API.
.NET (for IronPython):
IronPython enables integration with .NET libraries.
10. Debugging and Profiling Tools
Inspecting Python Internals:
Use tools like sys, gc, and inspect to analyze object references and Python's memory usage.
Line-by-Line Profiling:
Tools like line_profiler give granular performance insights.
11. Practice Resources
Hands-On:
Write Python scripts and analyze the bytecode with dis.
Explore ASTs by parsing code snippets.
Books:
Fluent Python by Luciano Ramalho.
Python Cookbook by David Beazley.
