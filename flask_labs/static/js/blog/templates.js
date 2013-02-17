(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['post'] = template(function (Handlebars,depth0,helpers,partials,data) {
  this.compilerInfo = [2,'>= 1.0.0-rc.3'];
helpers = helpers || Handlebars.helpers; data = data || {};
  var buffer = "", stack1, stack2, functionType="function", escapeExpression=this.escapeExpression, self=this;

function program1(depth0,data) {
  
  var buffer = "", stack1;
  buffer += "\n          <h2 class=\"subheading\">"
    + escapeExpression(((stack1 = ((stack1 = depth0.post),stack1 == null || stack1 === false ? stack1 : stack1.subtitle)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1))
    + "</h2>\n        ";
  return buffer;
  }

function program3(depth0,data) {
  
  var buffer = "", stack1;
  buffer += "\n        <div id=\"quotation\">\n            <blockquote id=\"header-quote\">"
    + escapeExpression(((stack1 = ((stack1 = ((stack1 = depth0.post),stack1 == null || stack1 === false ? stack1 : stack1.quote)),stack1 == null || stack1 === false ? stack1 : stack1.quote)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1))
    + "</blockquote>\n            <cite id=\"header-cite\">"
    + escapeExpression(((stack1 = ((stack1 = ((stack1 = depth0.post),stack1 == null || stack1 === false ? stack1 : stack1.quote)),stack1 == null || stack1 === false ? stack1 : stack1.source)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1))
    + "</cite>\n        </div>\n        ";
  return buffer;
  }

  buffer += "<div class=\"grid_col_3\">&nbsp;</div>\n    <article id='post' class=\"grid_col_9\">\n    <header>\n        <aside class=\"pub-date\">DATE</aside>\n        <h1 id=\"title\">"
    + escapeExpression(((stack1 = ((stack1 = depth0.post),stack1 == null || stack1 === false ? stack1 : stack1.title)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1))
    + "</h1>\n        ";
  stack2 = helpers['if'].call(depth0, ((stack1 = depth0.post),stack1 == null || stack1 === false ? stack1 : stack1.subtitle), {hash:{},inverse:self.noop,fn:self.program(1, program1, data),data:data});
  if(stack2 || stack2 === 0) { buffer += stack2; }
  buffer += "\n        ";
  stack2 = helpers['if'].call(depth0, ((stack1 = depth0.post),stack1 == null || stack1 === false ? stack1 : stack1.quote), {hash:{},inverse:self.noop,fn:self.program(3, program3, data),data:data});
  if(stack2 || stack2 === 0) { buffer += stack2; }
  buffer += "\n    </header>\n    <div id=\"copy\">\n        ";
  stack2 = ((stack1 = ((stack1 = depth0.post),stack1 == null || stack1 === false ? stack1 : stack1.html)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1);
  if(stack2 || stack2 === 0) { buffer += stack2; }
  buffer += "\n    </div>\n</article>\n";
  return buffer;
  });
templates['section'] = template(function (Handlebars,depth0,helpers,partials,data) {
  this.compilerInfo = [2,'>= 1.0.0-rc.3'];
helpers = helpers || Handlebars.helpers; data = data || {};
  var buffer = "", stack1, stack2, functionType="function", escapeExpression=this.escapeExpression, self=this;

function program1(depth0,data) {
  
  var buffer = "", stack1, stack2;
  buffer += "\n    <li class=\"post_listing\">\n        <h2 class=\"post_title\">\n            <a class=\"permalink\" href=\"";
  if (stack1 = helpers.uri) { stack1 = stack1.call(depth0, {hash:{},data:data}); }
  else { stack1 = depth0.uri; stack1 = typeof stack1 === functionType ? stack1.apply(depth0) : stack1; }
  buffer += escapeExpression(stack1)
    + "\">\n                <span class=\"post_heading\">";
  if (stack1 = helpers.title) { stack1 = stack1.call(depth0, {hash:{},data:data}); }
  else { stack1 = depth0.title; stack1 = typeof stack1 === functionType ? stack1.apply(depth0) : stack1; }
  buffer += escapeExpression(stack1)
    + "</span><br>\n                ";
  stack1 = helpers['if'].call(depth0, depth0.subtitle, {hash:{},inverse:self.noop,fn:self.program(2, program2, data),data:data});
  if(stack1 || stack1 === 0) { buffer += stack1; }
  buffer += "\n            </a>\n        </h2>\n        <div class=\"pub-date\">"
    + escapeExpression(((stack1 = ((stack1 = depth0.create_date),stack1 == null || stack1 === false ? stack1 : stack1.date)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1))
    + "</div>\n        ";
  stack2 = helpers['if'].call(depth0, depth0.tags, {hash:{},inverse:self.noop,fn:self.program(4, program4, data),data:data});
  if(stack2 || stack2 === 0) { buffer += stack2; }
  buffer += "\n\n        ";
  stack2 = helpers['if'].call(depth0, depth0.teaser, {hash:{},inverse:self.noop,fn:self.program(7, program7, data),data:data});
  if(stack2 || stack2 === 0) { buffer += stack2; }
  buffer += "\n    </li>\n    ";
  return buffer;
  }
function program2(depth0,data) {
  
  var buffer = "", stack1;
  buffer += "\n                <span class=\"subheading\">";
  if (stack1 = helpers.subtitle) { stack1 = stack1.call(depth0, {hash:{},data:data}); }
  else { stack1 = depth0.subtitle; stack1 = typeof stack1 === functionType ? stack1.apply(depth0) : stack1; }
  buffer += escapeExpression(stack1)
    + "</span>\n                ";
  return buffer;
  }

function program4(depth0,data) {
  
  var buffer = "", stack1;
  buffer += "\n            <ul class=\"tags\">\n            ";
  stack1 = helpers.each.call(depth0, depth0.tags, {hash:{},inverse:self.noop,fn:self.program(5, program5, data),data:data});
  if(stack1 || stack1 === 0) { buffer += stack1; }
  buffer += "\n            </ul>\n        ";
  return buffer;
  }
function program5(depth0,data) {
  
  var buffer = "";
  buffer += "\n                <li class='tag'>"
    + escapeExpression((typeof depth0 === functionType ? depth0.apply(depth0) : depth0))
    + "</li>\n            ";
  return buffer;
  }

function program7(depth0,data) {
  
  var buffer = "", stack1;
  buffer += "<p class=\"teaser\">";
  if (stack1 = helpers.teaser) { stack1 = stack1.call(depth0, {hash:{},data:data}); }
  else { stack1 = depth0.teaser; stack1 = typeof stack1 === functionType ? stack1.apply(depth0) : stack1; }
  buffer += escapeExpression(stack1)
    + "</p>";
  return buffer;
  }

  buffer += "<div class=\"grid_col_3\"><h1 id=\"title\">"
    + escapeExpression(((stack1 = ((stack1 = depth0.section),stack1 == null || stack1 === false ? stack1 : stack1.name)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1))
    + "</h1>\n    </div>\n<div class=\"grid_col_9\">\n    <ul class=\"posts_listing\">\n    ";
  stack2 = helpers.each.call(depth0, ((stack1 = depth0.section),stack1 == null || stack1 === false ? stack1 : stack1.posts), {hash:{},inverse:self.noop,fn:self.program(1, program1, data),data:data});
  if(stack2 || stack2 === 0) { buffer += stack2; }
  buffer += "\n\n    </ul>\n</div>\n";
  return buffer;
  });
})();