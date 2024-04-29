def summary_picker(model, params=[], bse=[], rsquared=False, rsquared_adj=False, pvalues=[]):
  string_to_print = ""
  if params:
    string_to_print += "\n"
    string_to_print += "Coefficient Values:\n"
    for val in params:
      string_to_print += val + " --> " + str(model.params[val]) + "\n"

  if bse:
    string_to_print += "\n"
    string_to_print += "Standar Error Values:\n"
    for val in bse:
      string_to_print += val + " --> " + str(model.bse[val]) + "\n"

  if rsquared:
    string_to_print += "\n"
    string_to_print += "R-squared --> " + str(rsquared) + "\n"

  if rsquared_adj:
    string_to_print += "\n"
    string_to_print += "Adjusted R-squared --> " + str(rsquared_adj) + "\n"

  if pvalues:
    string_to_print += "\n"
    string_to_print += "P-Values:\n"
    for val in pvalues:
      string_to_print += val + " --> " + str(model.pvalues[val]) + "\n"

  return string_to_print
