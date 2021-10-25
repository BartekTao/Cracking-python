

def determine_build_order(projects, dependencies):
    dependencies_project = {p : {} for p in projects}
    unorder_projects = set(projects)
    order_proect = []

    for (dependency, project) in dependencies:
        dependencies_project[project] = dependency
    
    while unorder_projects:
        for project in list(unorder_projects):
            if not dependencies_project[project]:
                order_proect.append(project)
                unorder_projects.remove(project)
        




class Project:
    def __init__(self, name) -> None:
        self.name = name
        self.dependencyChild = []
        self.dependencyChildMap = {}
        self.dependencies = 0
    
    def addDependencyChild(self, project):
        if project.name not in self.dependencyChildMap:
            project.incrementDependencies()
            self.dependencyChild.append(project)
            self.dependencyChildMap[project.name] = project
    
    def incrementDependencies(self):
        self.dependencies+=1

    def decrementDependencies(self):
        self.dependencies-=1

    
class Graph:
    def __init__(self, projects):
        self.nodes = []
        self.dic = {p : {} for p in projects}

    def getOrCreateNode(self, name) -> Project:
        if not self.dic[name]:
            project = Project(name)
            self.dic[name] = project
            self.nodes.append(project)

        return self.dic[name]

    def addEdge(self, dependencyName, projectName):
        dependency = self.getOrCreateNode(dependencyName)
        project = self.getOrCreateNode(projectName)
        dependency.addDependencyChild(project)

def buildGraph(projects, dependencies):
    graph = Graph(projects)
    
    for (dependency, project) in dependencies:
        graph.addEdge(dependency, project)
    return graph

def addNoneDenpendencies(order, projects, offset) -> int:
    for p in projects:
        if p.dependencies == 0:
            order.append(p)
            offset+=1
    return offset

def buildOrder(prejects):
    order = []

    endOfList = addNoneDenpendencies(order, prejects, 0)

    toBeProcess = 0
    while toBeProcess < len(order):
        curr = order[toBeProcess]

        if not curr:
            return None
        
        for child in curr.dependencyChild:
            child.decrementDependencies()
        
        endOfList = addNoneDenpendencies(order, curr.dependencyChild, endOfList)

        toBeProcess+=1
    return order

    






class NoValidBuildOrderError(Exception):
    pass

if __name__ == "__main__":
    projects = ["a", "b", "c", "d", "e", "f", "g"]
    dependencies = [
        ("d", "g"),
        ("a", "e"),
        ("b", "e"),
        ("c", "a"),
        ("f", "a"),
        ("b", "a"),
        ("f", "c"),
        ("f", "b"),
    ]
    graph = buildGraph(projects, dependencies)
    build_order = buildOrder(graph.nodes)
    map(build_order)
    for o in build_order:
        print(o.name)
    for dependency, project in dependencies:
        assert build_order.index(dependency) < build_order.index(project)
        
    #build_order = determine_build_order(projects, dependencies)