# -*- coding: utf-8 -*-
"""Social Network Analysis Module.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NmnFMMSDFiOwqQ6Wt8RYyaG57if3DBfI
"""

class sna:

  def handover_of_work(log):
#https://github.com/pm4py/pm4py-core/blob/74eb2a5977db7f28183ac74dbb5bb6f59570d479/pm4py/algo/organizational_mining/sna/algorithm.py
#https://github.com/pm4py/pm4py-core/blob/74eb2a5977db7f28183ac74dbb5bb6f59570d479/pm4py/org.py#L124
    from pm4py.visualization.sna import visualizer as sna_vis
    #from pm4py.algo.enhancement.sna import factory as sna_factory
    from pm4py.algo.organizational_mining.sna import algorithm as sna_factory

    ## networkx is a library for social network analysis
    import networkx as nx
    ## Create the handover network using the log
    handover_nw = sna_factory.log_handover.apply(log)
    ## Generate the network visualisation
    gviz_hw_py = sna_vis.networkx.apply(handover_nw)


    ## Display the network
    return sna_vis.networkx.view(gviz_hw_py)

  def subcontracting(log):
    from pm4py import org
    from pm4py.visualization.sna import visualizer as sub_vis
    ## networkx is a library for social network analysis
    import networkx as nx
    ## Create the handover network using the log
    
    subcontracting = org.discover_subcontracting_network(log)
    ## Generate the network visualisation
    gviz_subcontracting_py = sub_vis.networkx.apply(subcontracting)

    
    ## Display the network
    return sub_vis.networkx.view(gviz_subcontracting_py)
  

  def working_together(log):
    from pm4py import org
    from pm4py.visualization.sna import visualizer as work_tog_vis
    ## networkx is a library for social network analysis
    import networkx as nx
    ## Create the handover network using the log
    working_together = org.discover_working_together_network(log)
    ## Generate the network visualisation
    gviz_work_together_py = work_tog_vis.networkx.apply(working_together)

    
    ## Display the network
    return work_tog_vis.networkx.view(gviz_work_together_py)







  def similar_activities(log):
    from pm4py import org
    from pm4py.visualization.sna import visualizer as sim_act_vis
    ## networkx is a library for social network analysis
    import networkx as nx
    ## Create the handover network using the log
    similar_activities = org.discover_activity_based_resource_similarity(log)
    ## Generate the network visualisation
    gviz_simact_py = sim_act_vis.networkx.apply(similar_activities)

    
    ## Display the network
    return sim_act_vis.networkx.view(gviz_simact_py)






  def role_discovery(log):
    from pm4py import org
    from pm4py.visualization.sna import visualizer as role_vis
    ## networkx is a library for social network analysis
    import networkx as nx
    ## Create the handover network using the log
    roles = org.discover_organizational_roles(log)

    # prints a list of a set of activities in the log that are executed by a similar (multi)set of resources. 
    [print(i) for i in roles]






  def clustering(log):
    #Clustering the results of the working together metric, individuals that work often together would be inserted in the same group.
    #Clustering the results of the similar activities metric, individuals that work on the same tasks would be inserted in the same group.
    from pm4py import org
    ## Create clustering using the log
    similar_activities = org.discover_activity_based_resource_similarity(log)
    working_together = org.discover_working_together_network(log)

    from pm4py.algo.organizational_mining.sna import util
    similar_activity_cluster_metric = util.cluster_affinity_propagation(similar_activities)
    working_together_cluster_metric = util.cluster_affinity_propagation(working_together)


    return print('clustered similar activities metric: {}\n working together clustered metric: {}'.format(similar_activity_cluster_metric,working_together_cluster_metric) )




  def organizational_mining(log):
    from pm4py.algo.organizational_mining.local_diagnostics import algorithm as local_diagnostics

      # this applies the organizational mining from an attribute that is in each event, describing the group that is performing the task.
    ld = local_diagnostics.apply_from_group_attribute(log, parameters={local_diagnostics.Parameters.GROUP_KEY: "org:resource"})
      # GROUP RELATIVE FOCUS (on a given type of work) specifies how much a resource group performed this type of work
      # compared to the overall workload of the group. It can be used to measure how the workload of a resource group
      # is distributed over different types of work, i.e., work diversification of the group.
    print("\ngroup_relative_focus")
    print(ld["group_relative_focus"])
      # GROUP RELATIVE STAKE (in a given type of work) specifies how much this type of work was performed by a certain
      # resource group among all groups. It can be used to measure how the workload devoted to a certain type of work is
      # distributed over resource groups in an organizational model, i.e., work participation by different groups.
    print("\ngroup_relative_stake")
    print(ld["group_relative_stake"])
      # GROUP COVERAGE with respect to a given type of work specifies the proportion of members of a resource group that
      # performed this type of work.
    print("\ngroup_coverage")
    print(ld["group_coverage"])
      # GROUP MEMBER CONTRIBUTION of a member of a resource group with respect to the given type of work specifies how
      # much of this type of work by the group was performed by the member. It can be used to measure how the workload
      # of the entire group devoted to a certain type of work is distributed over the group members.
    print("\ngroup_member_contribution")
    print(ld["group_member_contribution"])